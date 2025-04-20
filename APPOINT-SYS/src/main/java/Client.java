import com.example.hospital.*;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.util.List;

/**
 * @author shuimqy
 * @version 1.0
 */
public class Client {
    public static void main(String[] args) {
//        构建一个通信管道，使用明文通信
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost",8189)
                .usePlaintext()
                .build();
//        使用阻塞式存根
        HospitalServiceGrpc.HospitalServiceBlockingStub stub= HospitalServiceGrpc.newBlockingStub(channel);
//       验证bookAppointment方法
//        构建请求消息
        Appointment appointment= Appointment.newBuilder().setPatientName("小明")
                .build();
        OperationResponse response=stub.bookAppointment(appointment);
        System.out.println(response.getMessage());
//        验证queryById方法
        AppointmentIDRequest request1=AppointmentIDRequest.newBuilder().setId(1)
                .build();
        Appointment response1=stub.queryByID(request1);
        System.out.println(response1.getPatientName());
//        验证QueryByPatient方法
        PatientRequest request=PatientRequest.newBuilder().setPatientName("小明")
                .build();
        AppointmentList response2=stub.queryByPatient(request);
        List<Appointment> appointmentList=response2.getAppointmentsList();
        for (Appointment value : appointmentList) {
            System.out.println(value.getPatientName());
        }
//        验证cancelAppointment方法
        AppointmentIDRequest request2=AppointmentIDRequest.newBuilder().setId(1)
                .build();
        OperationResponse response3=stub.cancelAppointment(request2);
        System.out.println(response3.getMessage());
    }
}
