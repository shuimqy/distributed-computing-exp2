import com.example.hospital.*;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.util.concurrent.ConcurrentHashMap;

/**
 * @author shuimqy
 * @version 1.0
 */
public class HospitalServer {

//    使用线程安全的hashmap来存储预约数据
private static final ConcurrentHashMap<Integer, Appointment> appointmentsStore = new ConcurrentHashMap<>();
//    创建id到姓名的映射
private  static final  ConcurrentHashMap<Integer,String> IdNameStore=new ConcurrentHashMap<>();
//    创建姓名到id的映射
private  static final  ConcurrentHashMap<String,Integer> NameIdStore=new ConcurrentHashMap<>();

    public static void main(String[] args) throws Exception {
//        添加并启动监听
        Server server= ServerBuilder.forPort(8189)
                .addService(new HospitalImpl())
                .build()
                .start();
        server.awaitTermination();
    }
    static class HospitalImpl extends HospitalServiceGrpc.HospitalServiceImplBase{
        int ID=0;
//        实现id方法（ID自加1）
        int IDaa(){
            ++ID;
            return ID;
        }
//        重写方法以实现接口
        @Override
        public void bookAppointment(Appointment request, StreamObserver<OperationResponse> responseObserver) {
//            接收预约信息，添加id，进行存储
//            Appointment ByIdAppointment=request.toBuilder().setId(IDaa()).build();
            appointmentsStore.put(request.getId(),request);
//            添加name到 id映射
            NameIdStore.put(request.getPatientName(),request.getId());
//            添加id到name映射
            IdNameStore.put(request.getId(),request.getPatientName());
//            构造响应消息，并发送给客户端
            OperationResponse response=OperationResponse.newBuilder()
                    .setSuccess(true)
                    .setMessage("book appointment success!")
                    .build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
//          实现根据ID查询方法
        @Override
        public void queryByID(AppointmentIDRequest request, StreamObserver<Appointment> responseObserver) {
            int id=request.getId();
            Appointment appointmentRequest=appointmentsStore.get(id);
            responseObserver.onNext(appointmentRequest);
            responseObserver.onCompleted();
        }
//        实现queryByPatient方法

        @Override
        public void queryByPatient(PatientRequest request, StreamObserver<AppointmentList> responseObserver) {
            AppointmentList response=AppointmentList.newBuilder().addAppointments(appointmentsStore.get(NameIdStore.get(request.getPatientName())))
                    .build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }

        @Override
        public void cancelAppointment(AppointmentIDRequest request, StreamObserver<OperationResponse> responseObserver) {
            int id=request.getId();
            String name=IdNameStore.get(id);
            appointmentsStore.remove(id);
            IdNameStore.remove(id);
            NameIdStore.remove(name);
            OperationResponse response =OperationResponse.newBuilder().setSuccess(true)
                    .setMessage("cancel success")
                    .build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
    }
}
