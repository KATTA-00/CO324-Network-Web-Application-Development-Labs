# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: door.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndoor.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x16\n\x05\x45vent\x12\r\n\x05\x65vent\x18\x01 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"-\n\x14\x43urrentStateResponse\x12\x15\n\rcurrent_state\x18\x01 \x01(\t2k\n\x04\x44oor\x12!\n\x0cProcessEvent\x12\x06.Event\x1a\t.Response\x12@\n\x0fGetCurrentState\x12\x16.google.protobuf.Empty\x1a\x15.CurrentStateResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'door_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EVENT']._serialized_start=43
  _globals['_EVENT']._serialized_end=65
  _globals['_RESPONSE']._serialized_start=67
  _globals['_RESPONSE']._serialized_end=94
  _globals['_CURRENTSTATERESPONSE']._serialized_start=96
  _globals['_CURRENTSTATERESPONSE']._serialized_end=141
  _globals['_DOOR']._serialized_start=143
  _globals['_DOOR']._serialized_end=250
# @@protoc_insertion_point(module_scope)