"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Appointment(google.protobuf.message.Message):
    """领域对象"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PATIENT_NAME_FIELD_NUMBER: builtins.int
    DOCTOR_NAME_FIELD_NUMBER: builtins.int
    DEPARTMENT_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    TIME_SLOT_FIELD_NUMBER: builtins.int
    id: builtins.int
    patient_name: builtins.str
    doctor_name: builtins.str
    department: builtins.str
    date: builtins.str
    """日期格式：YYYY-MM-DD"""
    time_slot: builtins.str
    """时间段如 "14:00-15:00" """
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        patient_name: builtins.str = ...,
        doctor_name: builtins.str = ...,
        department: builtins.str = ...,
        date: builtins.str = ...,
        time_slot: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["date", b"date", "department", b"department", "doctor_name", b"doctor_name", "id", b"id", "patient_name", b"patient_name", "time_slot", b"time_slot"]) -> None: ...

global___Appointment = Appointment

@typing.final
class AppointmentIDRequest(google.protobuf.message.Message):
    """请求/响应结构"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.int
    def __init__(
        self,
        *,
        id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___AppointmentIDRequest = AppointmentIDRequest

@typing.final
class PatientRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATIENT_NAME_FIELD_NUMBER: builtins.int
    patient_name: builtins.str
    def __init__(
        self,
        *,
        patient_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["patient_name", b"patient_name"]) -> None: ...

global___PatientRequest = PatientRequest

@typing.final
class OperationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    success: builtins.bool
    message: builtins.str
    """操作结果描述"""
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["message", b"message", "success", b"success"]) -> None: ...

global___OperationResponse = OperationResponse

@typing.final
class AppointmentList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    APPOINTMENTS_FIELD_NUMBER: builtins.int
    @property
    def appointments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Appointment]: ...
    def __init__(
        self,
        *,
        appointments: collections.abc.Iterable[global___Appointment] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["appointments", b"appointments"]) -> None: ...

global___AppointmentList = AppointmentList
