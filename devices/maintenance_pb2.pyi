import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaintenanceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUNNING: _ClassVar[MaintenanceStatus]
    FINISHED: _ClassVar[MaintenanceStatus]
    CANCELED: _ClassVar[MaintenanceStatus]
    ACCEPTED: _ClassVar[MaintenanceStatus]
RUNNING: MaintenanceStatus
FINISHED: MaintenanceStatus
CANCELED: MaintenanceStatus
ACCEPTED: MaintenanceStatus

class Maintenance(_message.Message):
    __slots__ = ("id", "device_id", "service_id", "organization_id", "created_by", "updated_by", "started_mileage", "started_uptime", "started_at", "expires_at", "uptime", "mileage", "finished_at", "current_uptime", "current_mileage", "status", "created_at", "updated_at", "service")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    STARTED_MILEAGE_FIELD_NUMBER: _ClassVar[int]
    STARTED_UPTIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_UPTIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MILEAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    id: int
    device_id: int
    service_id: int
    organization_id: int
    created_by: int
    updated_by: int
    started_mileage: int
    started_uptime: int
    started_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    uptime: int
    mileage: int
    finished_at: _timestamp_pb2.Timestamp
    current_uptime: int
    current_mileage: int
    status: MaintenanceStatus
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    service: MaintenanceService
    def __init__(self, id: _Optional[int] = ..., device_id: _Optional[int] = ..., service_id: _Optional[int] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., updated_by: _Optional[int] = ..., started_mileage: _Optional[int] = ..., started_uptime: _Optional[int] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., uptime: _Optional[int] = ..., mileage: _Optional[int] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., current_uptime: _Optional[int] = ..., current_mileage: _Optional[int] = ..., status: _Optional[_Union[MaintenanceStatus, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., service: _Optional[_Union[MaintenanceService, _Mapping]] = ...) -> None: ...

class MaintenanceService(_message.Message):
    __slots__ = ("id", "name", "organization_id", "created_by", "updated_by", "is_default", "expire_mileage_period", "expire_date_period", "expire_active_duration_period", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_MILEAGE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_DATE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_ACTIVE_DURATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    organization_id: int
    created_by: int
    updated_by: int
    is_default: bool
    expire_mileage_period: int
    expire_date_period: _timestamp_pb2.Timestamp
    expire_active_duration_period: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., updated_by: _Optional[int] = ..., is_default: bool = ..., expire_mileage_period: _Optional[int] = ..., expire_date_period: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expire_active_duration_period: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
