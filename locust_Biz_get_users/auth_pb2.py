# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\".\n\tMyRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12\r\n\x05nonce\x18\x02 \x01(\t\"[\n\nMyResponse\x12\r\n\x05nonce\x18\x01 \x01(\t\x12\x14\n\x0cserver_nonce\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\x05\x12\t\n\x01p\x18\x04 \x01(\t\x12\t\n\x01g\x18\x05 \x01(\t26\n\tMyService\x12)\n\x0eProcessRequest\x12\n.MyRequest\x1a\x0b.MyResponseB\x0eZ\x0c/authserviceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014/authservice'
  _MYREQUEST._serialized_start=14
  _MYREQUEST._serialized_end=60
  _MYRESPONSE._serialized_start=62
  _MYRESPONSE._serialized_end=153
  _MYSERVICE._serialized_start=155
  _MYSERVICE._serialized_end=209
# @@protoc_insertion_point(module_scope)
