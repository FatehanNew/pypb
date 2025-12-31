import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataModule(_message.Message):
    __slots__ = ("modules",)
    class ModuleList(_message.Message):
        __slots__ = ("tpms",)
        TPMS_FIELD_NUMBER: _ClassVar[int]
        tpms: TirePressureMonitoringSystemModule
        def __init__(self, tpms: _Optional[_Union[TirePressureMonitoringSystemModule, _Mapping]] = ...) -> None: ...
    MODULES_FIELD_NUMBER: _ClassVar[int]
    modules: _containers.RepeatedCompositeFieldContainer[DataModule.ModuleList]
    def __init__(self, modules: _Optional[_Iterable[_Union[DataModule.ModuleList, _Mapping]]] = ...) -> None: ...

class TirePressureMonitoringSystemModule(_message.Message):
    __slots__ = ("tire_axle_key", "pressure_key", "temperature_key", "status_key", "tire_data")
    class Position(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RIGHT_OUT: _ClassVar[TirePressureMonitoringSystemModule.Position]
        RIGHT_IN: _ClassVar[TirePressureMonitoringSystemModule.Position]
        LEFT_IN: _ClassVar[TirePressureMonitoringSystemModule.Position]
        LEFT_OUT: _ClassVar[TirePressureMonitoringSystemModule.Position]
    RIGHT_OUT: TirePressureMonitoringSystemModule.Position
    RIGHT_IN: TirePressureMonitoringSystemModule.Position
    LEFT_IN: TirePressureMonitoringSystemModule.Position
    LEFT_OUT: TirePressureMonitoringSystemModule.Position
    class TirePosition(_message.Message):
        __slots__ = ("axle", "tire", "pressure", "temperature", "status", "updated_at", "position")
        AXLE_FIELD_NUMBER: _ClassVar[int]
        TIRE_FIELD_NUMBER: _ClassVar[int]
        PRESSURE_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        axle: int
        tire: int
        pressure: float
        temperature: float
        status: int
        updated_at: _timestamp_pb2.Timestamp
        position: TirePressureMonitoringSystemModule.Position
        def __init__(self, axle: _Optional[int] = ..., tire: _Optional[int] = ..., pressure: _Optional[float] = ..., temperature: _Optional[float] = ..., status: _Optional[int] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., position: _Optional[_Union[TirePressureMonitoringSystemModule.Position, str]] = ...) -> None: ...
    class TireDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TirePressureMonitoringSystemModule.TirePosition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TirePressureMonitoringSystemModule.TirePosition, _Mapping]] = ...) -> None: ...
    TIRE_AXLE_KEY_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_KEY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATUS_KEY_FIELD_NUMBER: _ClassVar[int]
    TIRE_DATA_FIELD_NUMBER: _ClassVar[int]
    tire_axle_key: int
    pressure_key: int
    temperature_key: int
    status_key: int
    tire_data: _containers.MessageMap[int, TirePressureMonitoringSystemModule.TirePosition]
    def __init__(self, tire_axle_key: _Optional[int] = ..., pressure_key: _Optional[int] = ..., temperature_key: _Optional[int] = ..., status_key: _Optional[int] = ..., tire_data: _Optional[_Mapping[int, TirePressureMonitoringSystemModule.TirePosition]] = ...) -> None: ...
