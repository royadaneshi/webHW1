# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_users_with_sql_inject.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fget_users_with_sql_inject.proto\"]\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x12\x0b\n\x03sex\x18\x05 \x01(\t\x12\x11\n\tcreatedAt\x18\x06 \x01(\t\"G\n\x0eGetDataRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08\x61uth_key\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\x05\"B\n\x0fGetDataResponse\x12\x1b\n\x0creturn_users\x18\x01 \x03(\x0b\x32\x05.User\x12\x12\n\nmessage_id\x18\x02 \x01(\x05\x32;\n\tget_users\x12.\n\x07GetData\x12\x0f.GetDataRequest\x1a\x10.GetDataResponse\"\x00\x42$Z\"get_users_with_sql_inject_proto/pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_users_with_sql_inject_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\"get_users_with_sql_inject_proto/pb'
  _USER._serialized_start=35
  _USER._serialized_end=128
  _GETDATAREQUEST._serialized_start=130
  _GETDATAREQUEST._serialized_end=201
  _GETDATARESPONSE._serialized_start=203
  _GETDATARESPONSE._serialized_end=269
  _GET_USERS._serialized_start=271
  _GET_USERS._serialized_end=330
# @@protoc_insertion_point(module_scope)
