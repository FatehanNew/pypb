import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from areas import area_pb2 as _area_pb2
from devices import devices_pb2 as _devices_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkflowStat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING: _ClassVar[WorkflowStat]
    RUNNING: _ClassVar[WorkflowStat]
    FINISHED: _ClassVar[WorkflowStat]
    EXPIRED: _ClassVar[WorkflowStat]

class AreaEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[AreaEvent]
    ENTER: _ClassVar[AreaEvent]
    EXIT: _ClassVar[AreaEvent]
PENDING: WorkflowStat
RUNNING: WorkflowStat
FINISHED: WorkflowStat
EXPIRED: WorkflowStat
NONE: AreaEvent
ENTER: AreaEvent
EXIT: AreaEvent

class Workflow(_message.Message):
    __slots__ = ("id", "organization_id", "created_by", "name", "description", "flow", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    created_by: int
    name: str
    description: str
    flow: Flow
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., created_by: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., flow: _Optional[_Union[Flow, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class WorkflowTask(_message.Message):
    __slots__ = ("id", "organization_id", "workflow_id", "workflow_detail_id", "device_id", "flow", "pointer", "status", "starts_at", "expires_at", "created_at", "updated_at", "created_by", "confirmed_at", "rejected_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_DETAIL_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    POINTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    organization_id: int
    workflow_id: int
    workflow_detail_id: int
    device_id: int
    flow: Flow
    pointer: int
    status: WorkflowStat
    starts_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: int
    confirmed_at: _timestamp_pb2.Timestamp
    rejected_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., organization_id: _Optional[int] = ..., workflow_id: _Optional[int] = ..., workflow_detail_id: _Optional[int] = ..., device_id: _Optional[int] = ..., flow: _Optional[_Union[Flow, _Mapping]] = ..., pointer: _Optional[int] = ..., status: _Optional[_Union[WorkflowStat, str]] = ..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[int] = ..., confirmed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Flow(_message.Message):
    __slots__ = ("continuous", "last_gps_time", "events", "modules", "default_report", "payambar_report", "tanesh_report", "default_background", "payambar_background", "tanesh_background", "default_status", "tanesh_status")
    CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
    LAST_GPS_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_REPORT_FIELD_NUMBER: _ClassVar[int]
    PAYAMBAR_REPORT_FIELD_NUMBER: _ClassVar[int]
    TANESH_REPORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    PAYAMBAR_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    TANESH_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TANESH_STATUS_FIELD_NUMBER: _ClassVar[int]
    continuous: bool
    last_gps_time: int
    events: _containers.RepeatedCompositeFieldContainer[FlowEvent]
    modules: _containers.RepeatedCompositeFieldContainer[FlowModule]
    default_report: DefaultReport
    payambar_report: PayambarReport
    tanesh_report: TaneshReport
    default_background: DefaultBackground
    payambar_background: PayambarBackground
    tanesh_background: TaneshBackground
    default_status: DefaultStatus
    tanesh_status: TaneshStatus
    def __init__(self, continuous: bool = ..., last_gps_time: _Optional[int] = ..., events: _Optional[_Iterable[_Union[FlowEvent, _Mapping]]] = ..., modules: _Optional[_Iterable[_Union[FlowModule, _Mapping]]] = ..., default_report: _Optional[_Union[DefaultReport, _Mapping]] = ..., payambar_report: _Optional[_Union[PayambarReport, _Mapping]] = ..., tanesh_report: _Optional[_Union[TaneshReport, _Mapping]] = ..., default_background: _Optional[_Union[DefaultBackground, _Mapping]] = ..., payambar_background: _Optional[_Union[PayambarBackground, _Mapping]] = ..., tanesh_background: _Optional[_Union[TaneshBackground, _Mapping]] = ..., default_status: _Optional[_Union[DefaultStatus, _Mapping]] = ..., tanesh_status: _Optional[_Union[TaneshStatus, _Mapping]] = ...) -> None: ...

class TaneshStatus(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DefaultStatus(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FlowEvent(_message.Message):
    __slots__ = ("event", "event_trigger")
    class TriggerEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ON_FINISH: _ClassVar[FlowEvent.TriggerEvent]
        ON_START: _ClassVar[FlowEvent.TriggerEvent]
    ON_FINISH: FlowEvent.TriggerEvent
    ON_START: FlowEvent.TriggerEvent
    EVENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    event: FlowEvent.TriggerEvent
    event_trigger: NotificationTrigger
    def __init__(self, event: _Optional[_Union[FlowEvent.TriggerEvent, str]] = ..., event_trigger: _Optional[_Union[NotificationTrigger, _Mapping]] = ...) -> None: ...

class FlowModule(_message.Message):
    __slots__ = ("events", "area_module", "device_module")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    AREA_MODULE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODULE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[FlowEvent]
    area_module: AreaModule
    device_module: DeviceModule
    def __init__(self, events: _Optional[_Iterable[_Union[FlowEvent, _Mapping]]] = ..., area_module: _Optional[_Union[AreaModule, _Mapping]] = ..., device_module: _Optional[_Union[DeviceModule, _Mapping]] = ...) -> None: ...

class DefaultBackground(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PayambarBackground(_message.Message):
    __slots__ = ("moving_duration", "idling_duration", "parking_duration", "towing_duration")
    MOVING_DURATION_FIELD_NUMBER: _ClassVar[int]
    IDLING_DURATION_FIELD_NUMBER: _ClassVar[int]
    PARKING_DURATION_FIELD_NUMBER: _ClassVar[int]
    TOWING_DURATION_FIELD_NUMBER: _ClassVar[int]
    moving_duration: int
    idling_duration: int
    parking_duration: int
    towing_duration: int
    def __init__(self, moving_duration: _Optional[int] = ..., idling_duration: _Optional[int] = ..., parking_duration: _Optional[int] = ..., towing_duration: _Optional[int] = ...) -> None: ...

class TaneshBackground(_message.Message):
    __slots__ = ("main_area_id", "inside", "outside")
    class Item(_message.Message):
        __slots__ = ("duration", "moving_duration", "idling_duration", "parking_duration", "towing_duration", "total_mileage_at_start", "total_mileage_at_finish")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        MOVING_DURATION_FIELD_NUMBER: _ClassVar[int]
        IDLING_DURATION_FIELD_NUMBER: _ClassVar[int]
        PARKING_DURATION_FIELD_NUMBER: _ClassVar[int]
        TOWING_DURATION_FIELD_NUMBER: _ClassVar[int]
        TOTAL_MILEAGE_AT_START_FIELD_NUMBER: _ClassVar[int]
        TOTAL_MILEAGE_AT_FINISH_FIELD_NUMBER: _ClassVar[int]
        duration: int
        moving_duration: int
        idling_duration: int
        parking_duration: int
        towing_duration: int
        total_mileage_at_start: int
        total_mileage_at_finish: int
        def __init__(self, duration: _Optional[int] = ..., moving_duration: _Optional[int] = ..., idling_duration: _Optional[int] = ..., parking_duration: _Optional[int] = ..., towing_duration: _Optional[int] = ..., total_mileage_at_start: _Optional[int] = ..., total_mileage_at_finish: _Optional[int] = ...) -> None: ...
    MAIN_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    INSIDE_FIELD_NUMBER: _ClassVar[int]
    OUTSIDE_FIELD_NUMBER: _ClassVar[int]
    main_area_id: int
    inside: TaneshBackground.Item
    outside: TaneshBackground.Item
    def __init__(self, main_area_id: _Optional[int] = ..., inside: _Optional[_Union[TaneshBackground.Item, _Mapping]] = ..., outside: _Optional[_Union[TaneshBackground.Item, _Mapping]] = ...) -> None: ...

class AreaModule(_message.Message):
    __slots__ = ("starts", "finishes", "area_id", "running", "started_at", "finished_at", "total_mileage_at_start", "total_mileage_at_finish", "fuel_consumed_at_start", "fuel_consumed_at_finish", "max_speed", "total_speed", "count_speed", "duration", "moving_duration", "idling_duration", "parking_duration", "towing_duration", "minimum_accepted_duration", "area")
    STARTS_FIELD_NUMBER: _ClassVar[int]
    FINISHES_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MILEAGE_AT_START_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MILEAGE_AT_FINISH_FIELD_NUMBER: _ClassVar[int]
    FUEL_CONSUMED_AT_START_FIELD_NUMBER: _ClassVar[int]
    FUEL_CONSUMED_AT_FINISH_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    COUNT_SPEED_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MOVING_DURATION_FIELD_NUMBER: _ClassVar[int]
    IDLING_DURATION_FIELD_NUMBER: _ClassVar[int]
    PARKING_DURATION_FIELD_NUMBER: _ClassVar[int]
    TOWING_DURATION_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ACCEPTED_DURATION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    starts: AreaEvent
    finishes: AreaEvent
    area_id: int
    running: bool
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    total_mileage_at_start: int
    total_mileage_at_finish: int
    fuel_consumed_at_start: int
    fuel_consumed_at_finish: int
    max_speed: int
    total_speed: int
    count_speed: int
    duration: int
    moving_duration: int
    idling_duration: int
    parking_duration: int
    towing_duration: int
    minimum_accepted_duration: int
    area: _area_pb2.Area
    def __init__(self, starts: _Optional[_Union[AreaEvent, str]] = ..., finishes: _Optional[_Union[AreaEvent, str]] = ..., area_id: _Optional[int] = ..., running: bool = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_mileage_at_start: _Optional[int] = ..., total_mileage_at_finish: _Optional[int] = ..., fuel_consumed_at_start: _Optional[int] = ..., fuel_consumed_at_finish: _Optional[int] = ..., max_speed: _Optional[int] = ..., total_speed: _Optional[int] = ..., count_speed: _Optional[int] = ..., duration: _Optional[int] = ..., moving_duration: _Optional[int] = ..., idling_duration: _Optional[int] = ..., parking_duration: _Optional[int] = ..., towing_duration: _Optional[int] = ..., minimum_accepted_duration: _Optional[int] = ..., area: _Optional[_Union[_area_pb2.Area, _Mapping]] = ...) -> None: ...

class DeviceModule(_message.Message):
    __slots__ = ("starts", "finishes", "device_id", "radius", "running", "started_at", "finished_at", "total_mileage_at_start", "total_mileage_at_finish", "max_speed", "total_speed", "count_speed", "duration", "minimum_accepted_duration", "device")
    STARTS_FIELD_NUMBER: _ClassVar[int]
    FINISHES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MILEAGE_AT_START_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MILEAGE_AT_FINISH_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPEED_FIELD_NUMBER: _ClassVar[int]
    COUNT_SPEED_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ACCEPTED_DURATION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    starts: AreaEvent
    finishes: AreaEvent
    device_id: int
    radius: int
    running: bool
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    total_mileage_at_start: int
    total_mileage_at_finish: int
    max_speed: int
    total_speed: int
    count_speed: int
    duration: int
    minimum_accepted_duration: int
    device: _devices_pb2.Device
    def __init__(self, starts: _Optional[_Union[AreaEvent, str]] = ..., finishes: _Optional[_Union[AreaEvent, str]] = ..., device_id: _Optional[int] = ..., radius: _Optional[int] = ..., running: bool = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_mileage_at_start: _Optional[int] = ..., total_mileage_at_finish: _Optional[int] = ..., max_speed: _Optional[int] = ..., total_speed: _Optional[int] = ..., count_speed: _Optional[int] = ..., duration: _Optional[int] = ..., minimum_accepted_duration: _Optional[int] = ..., device: _Optional[_Union[_devices_pb2.Device, _Mapping]] = ...) -> None: ...

class DefaultReport(_message.Message):
    __slots__ = ("duration", "mileage", "started_at", "finished_at")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    duration: int
    mileage: int
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, duration: _Optional[int] = ..., mileage: _Optional[int] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PayambarReport(_message.Message):
    __slots__ = ("started_at", "finished_at", "mileage", "duration", "fuel_usage")
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FUEL_USAGE_FIELD_NUMBER: _ClassVar[int]
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    mileage: int
    duration: int
    fuel_usage: int
    def __init__(self, started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., mileage: _Optional[int] = ..., duration: _Optional[int] = ..., fuel_usage: _Optional[int] = ...) -> None: ...

class TaneshReport(_message.Message):
    __slots__ = ("started_at", "finished_at", "mileage", "duration")
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    MILEAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    mileage: int
    duration: int
    def __init__(self, started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., mileage: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class NotificationTrigger(_message.Message):
    __slots__ = ("user_id", "title", "body")
    class Via(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FCM: _ClassVar[NotificationTrigger.Via]
        SMS: _ClassVar[NotificationTrigger.Via]
        EMAIL: _ClassVar[NotificationTrigger.Via]
        DATABASE: _ClassVar[NotificationTrigger.Via]
    FCM: NotificationTrigger.Via
    SMS: NotificationTrigger.Via
    EMAIL: NotificationTrigger.Via
    DATABASE: NotificationTrigger.Via
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    title: str
    body: str
    def __init__(self, user_id: _Optional[int] = ..., title: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...
