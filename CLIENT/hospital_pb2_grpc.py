# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import hospital_pb2 as hospital__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in hospital_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class HospitalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BookAppointment = channel.unary_unary(
                '/HospitalService/BookAppointment',
                request_serializer=hospital__pb2.Appointment.SerializeToString,
                response_deserializer=hospital__pb2.OperationResponse.FromString,
                _registered_method=True)
        self.QueryByID = channel.unary_unary(
                '/HospitalService/QueryByID',
                request_serializer=hospital__pb2.AppointmentIDRequest.SerializeToString,
                response_deserializer=hospital__pb2.Appointment.FromString,
                _registered_method=True)
        self.QueryByPatient = channel.unary_unary(
                '/HospitalService/QueryByPatient',
                request_serializer=hospital__pb2.PatientRequest.SerializeToString,
                response_deserializer=hospital__pb2.AppointmentList.FromString,
                _registered_method=True)
        self.CancelAppointment = channel.unary_unary(
                '/HospitalService/CancelAppointment',
                request_serializer=hospital__pb2.AppointmentIDRequest.SerializeToString,
                response_deserializer=hospital__pb2.OperationResponse.FromString,
                _registered_method=True)


class HospitalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BookAppointment(self, request, context):
        """预约挂号
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryByID(self, request, context):
        """ID查询
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryByPatient(self, request, context):
        """患者查询
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelAppointment(self, request, context):
        """取消预约
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HospitalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BookAppointment': grpc.unary_unary_rpc_method_handler(
                    servicer.BookAppointment,
                    request_deserializer=hospital__pb2.Appointment.FromString,
                    response_serializer=hospital__pb2.OperationResponse.SerializeToString,
            ),
            'QueryByID': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryByID,
                    request_deserializer=hospital__pb2.AppointmentIDRequest.FromString,
                    response_serializer=hospital__pb2.Appointment.SerializeToString,
            ),
            'QueryByPatient': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryByPatient,
                    request_deserializer=hospital__pb2.PatientRequest.FromString,
                    response_serializer=hospital__pb2.AppointmentList.SerializeToString,
            ),
            'CancelAppointment': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelAppointment,
                    request_deserializer=hospital__pb2.AppointmentIDRequest.FromString,
                    response_serializer=hospital__pb2.OperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'HospitalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('HospitalService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HospitalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BookAppointment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/HospitalService/BookAppointment',
            hospital__pb2.Appointment.SerializeToString,
            hospital__pb2.OperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/HospitalService/QueryByID',
            hospital__pb2.AppointmentIDRequest.SerializeToString,
            hospital__pb2.Appointment.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryByPatient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/HospitalService/QueryByPatient',
            hospital__pb2.PatientRequest.SerializeToString,
            hospital__pb2.AppointmentList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CancelAppointment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/HospitalService/CancelAppointment',
            hospital__pb2.AppointmentIDRequest.SerializeToString,
            hospital__pb2.OperationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
