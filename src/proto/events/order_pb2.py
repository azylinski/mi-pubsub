# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events/order.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from events import user_pb2 as events_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='events/order.proto',
  package='events',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x65vents/order.proto\x12\x06\x65vents\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x11\x65vents/user.proto\"c\n\x05Order\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1e\n\x08\x63ustomer\x18\x64 \x01(\x0b\x32\x0c.events.Userb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,events_dot_user__pb2.DESCRIPTOR,])




_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='events.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_at', full_name='events.Order.created_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='events.Order.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer', full_name='events.Order.customer', index=2,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=181,
)

_ORDER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ORDER.fields_by_name['customer'].message_type = events_dot_user__pb2._USER
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), dict(
  DESCRIPTOR = _ORDER,
  __module__ = 'events.order_pb2'
  # @@protoc_insertion_point(class_scope:events.Order)
  ))
_sym_db.RegisterMessage(Order)


# @@protoc_insertion_point(module_scope)
