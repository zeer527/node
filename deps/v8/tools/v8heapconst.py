# Copyright 2018 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  34: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  42: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE",
  64: "STRING_TYPE",
  65: "CONS_STRING_TYPE",
  66: "EXTERNAL_STRING_TYPE",
  67: "SLICED_STRING_TYPE",
  69: "THIN_STRING_TYPE",
  72: "ONE_BYTE_STRING_TYPE",
  73: "CONS_ONE_BYTE_STRING_TYPE",
  74: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  75: "SLICED_ONE_BYTE_STRING_TYPE",
  77: "THIN_ONE_BYTE_STRING_TYPE",
  82: "EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  98: "UNCACHED_EXTERNAL_STRING_TYPE",
  106: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  114: "UNCACHED_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE",
  128: "SYMBOL_TYPE",
  129: "HEAP_NUMBER_TYPE",
  130: "BIGINT_TYPE",
  131: "ODDBALL_TYPE",
  132: "MAP_TYPE",
  133: "CODE_TYPE",
  134: "MUTABLE_HEAP_NUMBER_TYPE",
  135: "FOREIGN_TYPE",
  136: "BYTE_ARRAY_TYPE",
  137: "BYTECODE_ARRAY_TYPE",
  138: "FREE_SPACE_TYPE",
  139: "FIXED_INT8_ARRAY_TYPE",
  140: "FIXED_UINT8_ARRAY_TYPE",
  141: "FIXED_INT16_ARRAY_TYPE",
  142: "FIXED_UINT16_ARRAY_TYPE",
  143: "FIXED_INT32_ARRAY_TYPE",
  144: "FIXED_UINT32_ARRAY_TYPE",
  145: "FIXED_FLOAT32_ARRAY_TYPE",
  146: "FIXED_FLOAT64_ARRAY_TYPE",
  147: "FIXED_UINT8_CLAMPED_ARRAY_TYPE",
  148: "FIXED_BIGINT64_ARRAY_TYPE",
  149: "FIXED_BIGUINT64_ARRAY_TYPE",
  150: "FIXED_DOUBLE_ARRAY_TYPE",
  151: "FEEDBACK_METADATA_TYPE",
  152: "FILLER_TYPE",
  153: "ACCESS_CHECK_INFO_TYPE",
  154: "ACCESSOR_INFO_TYPE",
  155: "ACCESSOR_PAIR_TYPE",
  156: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  157: "ALLOCATION_MEMENTO_TYPE",
  158: "ASM_WASM_DATA_TYPE",
  159: "ASYNC_GENERATOR_REQUEST_TYPE",
  160: "DEBUG_INFO_TYPE",
  161: "FUNCTION_TEMPLATE_INFO_TYPE",
  162: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  163: "INTERCEPTOR_INFO_TYPE",
  164: "INTERPRETER_DATA_TYPE",
  165: "MODULE_INFO_ENTRY_TYPE",
  166: "MODULE_TYPE",
  167: "OBJECT_TEMPLATE_INFO_TYPE",
  168: "PROMISE_CAPABILITY_TYPE",
  169: "PROMISE_REACTION_TYPE",
  170: "PROTOTYPE_INFO_TYPE",
  171: "SCRIPT_TYPE",
  172: "STACK_FRAME_INFO_TYPE",
  173: "TUPLE2_TYPE",
  174: "TUPLE3_TYPE",
  175: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  176: "WASM_DEBUG_INFO_TYPE",
  177: "WASM_EXCEPTION_TAG_TYPE",
  178: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  179: "CALLABLE_TASK_TYPE",
  180: "CALLBACK_TASK_TYPE",
  181: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  182: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  183: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  184: "WEAK_FACTORY_CLEANUP_JOB_TASK_TYPE",
  185: "ALLOCATION_SITE_TYPE",
  186: "EMBEDDER_DATA_ARRAY_TYPE",
  187: "FIXED_ARRAY_TYPE",
  188: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  189: "HASH_TABLE_TYPE",
  190: "ORDERED_HASH_MAP_TYPE",
  191: "ORDERED_HASH_SET_TYPE",
  192: "ORDERED_NAME_DICTIONARY_TYPE",
  193: "NAME_DICTIONARY_TYPE",
  194: "GLOBAL_DICTIONARY_TYPE",
  195: "NUMBER_DICTIONARY_TYPE",
  196: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  197: "STRING_TABLE_TYPE",
  198: "EPHEMERON_HASH_TABLE_TYPE",
  199: "SCOPE_INFO_TYPE",
  200: "SCRIPT_CONTEXT_TABLE_TYPE",
  201: "AWAIT_CONTEXT_TYPE",
  202: "BLOCK_CONTEXT_TYPE",
  203: "CATCH_CONTEXT_TYPE",
  204: "DEBUG_EVALUATE_CONTEXT_TYPE",
  205: "EVAL_CONTEXT_TYPE",
  206: "FUNCTION_CONTEXT_TYPE",
  207: "MODULE_CONTEXT_TYPE",
  208: "NATIVE_CONTEXT_TYPE",
  209: "SCRIPT_CONTEXT_TYPE",
  210: "WITH_CONTEXT_TYPE",
  211: "WEAK_FIXED_ARRAY_TYPE",
  212: "TRANSITION_ARRAY_TYPE",
  213: "CALL_HANDLER_INFO_TYPE",
  214: "CELL_TYPE",
  215: "CODE_DATA_CONTAINER_TYPE",
  216: "DESCRIPTOR_ARRAY_TYPE",
  217: "FEEDBACK_CELL_TYPE",
  218: "FEEDBACK_VECTOR_TYPE",
  219: "LOAD_HANDLER_TYPE",
  220: "PREPARSE_DATA_TYPE",
  221: "PROPERTY_ARRAY_TYPE",
  222: "PROPERTY_CELL_TYPE",
  223: "SHARED_FUNCTION_INFO_TYPE",
  224: "SMALL_ORDERED_HASH_MAP_TYPE",
  225: "SMALL_ORDERED_HASH_SET_TYPE",
  226: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  227: "STORE_HANDLER_TYPE",
  228: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  229: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  230: "WEAK_ARRAY_LIST_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_VALUE_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_CELL_TYPE",
  1082: "JS_WEAK_REF_TYPE",
  1083: "JS_WEAK_FACTORY_CLEANUP_ITERATOR_TYPE",
  1084: "JS_WEAK_FACTORY_TYPE",
  1085: "JS_WEAK_MAP_TYPE",
  1086: "JS_WEAK_SET_TYPE",
  1087: "JS_TYPED_ARRAY_TYPE",
  1088: "JS_DATA_VIEW_TYPE",
  1089: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1090: "JS_INTL_COLLATOR_TYPE",
  1091: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1092: "JS_INTL_LIST_FORMAT_TYPE",
  1093: "JS_INTL_LOCALE_TYPE",
  1094: "JS_INTL_NUMBER_FORMAT_TYPE",
  1095: "JS_INTL_PLURAL_RULES_TYPE",
  1096: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1097: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1098: "JS_INTL_SEGMENTER_TYPE",
  1099: "WASM_EXCEPTION_TYPE",
  1100: "WASM_GLOBAL_TYPE",
  1101: "WASM_INSTANCE_TYPE",
  1102: "WASM_MEMORY_TYPE",
  1103: "WASM_MODULE_TYPE",
  1104: "WASM_TABLE_TYPE",
  1105: "JS_BOUND_FUNCTION_TYPE",
  1106: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("RO_SPACE", 0x00139): (138, "FreeSpaceMap"),
  ("RO_SPACE", 0x00189): (132, "MetaMap"),
  ("RO_SPACE", 0x00209): (131, "NullMap"),
  ("RO_SPACE", 0x00271): (216, "DescriptorArrayMap"),
  ("RO_SPACE", 0x002d1): (211, "WeakFixedArrayMap"),
  ("RO_SPACE", 0x00321): (152, "OnePointerFillerMap"),
  ("RO_SPACE", 0x00371): (152, "TwoPointerFillerMap"),
  ("RO_SPACE", 0x003f1): (131, "UninitializedMap"),
  ("RO_SPACE", 0x00461): (8, "OneByteInternalizedStringMap"),
  ("RO_SPACE", 0x00501): (131, "UndefinedMap"),
  ("RO_SPACE", 0x00561): (129, "HeapNumberMap"),
  ("RO_SPACE", 0x005e1): (131, "TheHoleMap"),
  ("RO_SPACE", 0x00689): (131, "BooleanMap"),
  ("RO_SPACE", 0x00761): (136, "ByteArrayMap"),
  ("RO_SPACE", 0x007b1): (187, "FixedArrayMap"),
  ("RO_SPACE", 0x00801): (187, "FixedCOWArrayMap"),
  ("RO_SPACE", 0x00851): (189, "HashTableMap"),
  ("RO_SPACE", 0x008a1): (128, "SymbolMap"),
  ("RO_SPACE", 0x008f1): (72, "OneByteStringMap"),
  ("RO_SPACE", 0x00941): (199, "ScopeInfoMap"),
  ("RO_SPACE", 0x00991): (223, "SharedFunctionInfoMap"),
  ("RO_SPACE", 0x009e1): (133, "CodeMap"),
  ("RO_SPACE", 0x00a31): (206, "FunctionContextMap"),
  ("RO_SPACE", 0x00a81): (214, "CellMap"),
  ("RO_SPACE", 0x00ad1): (222, "GlobalPropertyCellMap"),
  ("RO_SPACE", 0x00b21): (135, "ForeignMap"),
  ("RO_SPACE", 0x00b71): (212, "TransitionArrayMap"),
  ("RO_SPACE", 0x00bc1): (218, "FeedbackVectorMap"),
  ("RO_SPACE", 0x00c61): (131, "ArgumentsMarkerMap"),
  ("RO_SPACE", 0x00d01): (131, "ExceptionMap"),
  ("RO_SPACE", 0x00da1): (131, "TerminationExceptionMap"),
  ("RO_SPACE", 0x00e49): (131, "OptimizedOutMap"),
  ("RO_SPACE", 0x00ee9): (131, "StaleRegisterMap"),
  ("RO_SPACE", 0x00f59): (208, "NativeContextMap"),
  ("RO_SPACE", 0x00fa9): (207, "ModuleContextMap"),
  ("RO_SPACE", 0x00ff9): (205, "EvalContextMap"),
  ("RO_SPACE", 0x01049): (209, "ScriptContextMap"),
  ("RO_SPACE", 0x01099): (201, "AwaitContextMap"),
  ("RO_SPACE", 0x010e9): (202, "BlockContextMap"),
  ("RO_SPACE", 0x01139): (203, "CatchContextMap"),
  ("RO_SPACE", 0x01189): (210, "WithContextMap"),
  ("RO_SPACE", 0x011d9): (204, "DebugEvaluateContextMap"),
  ("RO_SPACE", 0x01229): (200, "ScriptContextTableMap"),
  ("RO_SPACE", 0x01279): (151, "FeedbackMetadataArrayMap"),
  ("RO_SPACE", 0x012c9): (187, "ArrayListMap"),
  ("RO_SPACE", 0x01319): (130, "BigIntMap"),
  ("RO_SPACE", 0x01369): (188, "ObjectBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x013b9): (137, "BytecodeArrayMap"),
  ("RO_SPACE", 0x01409): (215, "CodeDataContainerMap"),
  ("RO_SPACE", 0x01459): (150, "FixedDoubleArrayMap"),
  ("RO_SPACE", 0x014a9): (194, "GlobalDictionaryMap"),
  ("RO_SPACE", 0x014f9): (217, "ManyClosuresCellMap"),
  ("RO_SPACE", 0x01549): (187, "ModuleInfoMap"),
  ("RO_SPACE", 0x01599): (134, "MutableHeapNumberMap"),
  ("RO_SPACE", 0x015e9): (193, "NameDictionaryMap"),
  ("RO_SPACE", 0x01639): (217, "NoClosuresCellMap"),
  ("RO_SPACE", 0x01689): (217, "NoFeedbackCellMap"),
  ("RO_SPACE", 0x016d9): (195, "NumberDictionaryMap"),
  ("RO_SPACE", 0x01729): (217, "OneClosureCellMap"),
  ("RO_SPACE", 0x01779): (190, "OrderedHashMapMap"),
  ("RO_SPACE", 0x017c9): (191, "OrderedHashSetMap"),
  ("RO_SPACE", 0x01819): (192, "OrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01869): (220, "PreparseDataMap"),
  ("RO_SPACE", 0x018b9): (221, "PropertyArrayMap"),
  ("RO_SPACE", 0x01909): (213, "SideEffectCallHandlerInfoMap"),
  ("RO_SPACE", 0x01959): (213, "SideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019a9): (213, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("RO_SPACE", 0x019f9): (196, "SimpleNumberDictionaryMap"),
  ("RO_SPACE", 0x01a49): (187, "SloppyArgumentsElementsMap"),
  ("RO_SPACE", 0x01a99): (224, "SmallOrderedHashMapMap"),
  ("RO_SPACE", 0x01ae9): (225, "SmallOrderedHashSetMap"),
  ("RO_SPACE", 0x01b39): (226, "SmallOrderedNameDictionaryMap"),
  ("RO_SPACE", 0x01b89): (197, "StringTableMap"),
  ("RO_SPACE", 0x01bd9): (228, "UncompiledDataWithoutPreparseDataMap"),
  ("RO_SPACE", 0x01c29): (229, "UncompiledDataWithPreparseDataMap"),
  ("RO_SPACE", 0x01c79): (230, "WeakArrayListMap"),
  ("RO_SPACE", 0x01cc9): (198, "EphemeronHashTableMap"),
  ("RO_SPACE", 0x01d19): (186, "EmbedderDataArrayMap"),
  ("RO_SPACE", 0x01d69): (106, "NativeSourceStringMap"),
  ("RO_SPACE", 0x01db9): (64, "StringMap"),
  ("RO_SPACE", 0x01e09): (73, "ConsOneByteStringMap"),
  ("RO_SPACE", 0x01e59): (65, "ConsStringMap"),
  ("RO_SPACE", 0x01ea9): (77, "ThinOneByteStringMap"),
  ("RO_SPACE", 0x01ef9): (69, "ThinStringMap"),
  ("RO_SPACE", 0x01f49): (67, "SlicedStringMap"),
  ("RO_SPACE", 0x01f99): (75, "SlicedOneByteStringMap"),
  ("RO_SPACE", 0x01fe9): (66, "ExternalStringMap"),
  ("RO_SPACE", 0x02039): (82, "ExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02089): (74, "ExternalOneByteStringMap"),
  ("RO_SPACE", 0x020d9): (98, "UncachedExternalStringMap"),
  ("RO_SPACE", 0x02129): (114, "UncachedExternalStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02179): (0, "InternalizedStringMap"),
  ("RO_SPACE", 0x021c9): (2, "ExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02219): (18, "ExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02269): (10, "ExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x022b9): (34, "UncachedExternalInternalizedStringMap"),
  ("RO_SPACE", 0x02309): (50, "UncachedExternalInternalizedStringWithOneByteDataMap"),
  ("RO_SPACE", 0x02359): (42, "UncachedExternalOneByteInternalizedStringMap"),
  ("RO_SPACE", 0x023a9): (106, "UncachedExternalOneByteStringMap"),
  ("RO_SPACE", 0x023f9): (140, "FixedUint8ArrayMap"),
  ("RO_SPACE", 0x02449): (139, "FixedInt8ArrayMap"),
  ("RO_SPACE", 0x02499): (142, "FixedUint16ArrayMap"),
  ("RO_SPACE", 0x024e9): (141, "FixedInt16ArrayMap"),
  ("RO_SPACE", 0x02539): (144, "FixedUint32ArrayMap"),
  ("RO_SPACE", 0x02589): (143, "FixedInt32ArrayMap"),
  ("RO_SPACE", 0x025d9): (145, "FixedFloat32ArrayMap"),
  ("RO_SPACE", 0x02629): (146, "FixedFloat64ArrayMap"),
  ("RO_SPACE", 0x02679): (147, "FixedUint8ClampedArrayMap"),
  ("RO_SPACE", 0x026c9): (149, "FixedBigUint64ArrayMap"),
  ("RO_SPACE", 0x02719): (148, "FixedBigInt64ArrayMap"),
  ("RO_SPACE", 0x02769): (131, "SelfReferenceMarkerMap"),
  ("RO_SPACE", 0x027d1): (173, "Tuple2Map"),
  ("RO_SPACE", 0x02871): (175, "ArrayBoilerplateDescriptionMap"),
  ("RO_SPACE", 0x02bb1): (163, "InterceptorInfoMap"),
  ("RO_SPACE", 0x05081): (153, "AccessCheckInfoMap"),
  ("RO_SPACE", 0x050d1): (154, "AccessorInfoMap"),
  ("RO_SPACE", 0x05121): (155, "AccessorPairMap"),
  ("RO_SPACE", 0x05171): (156, "AliasedArgumentsEntryMap"),
  ("RO_SPACE", 0x051c1): (157, "AllocationMementoMap"),
  ("RO_SPACE", 0x05211): (158, "AsmWasmDataMap"),
  ("RO_SPACE", 0x05261): (159, "AsyncGeneratorRequestMap"),
  ("RO_SPACE", 0x052b1): (160, "DebugInfoMap"),
  ("RO_SPACE", 0x05301): (161, "FunctionTemplateInfoMap"),
  ("RO_SPACE", 0x05351): (162, "FunctionTemplateRareDataMap"),
  ("RO_SPACE", 0x053a1): (164, "InterpreterDataMap"),
  ("RO_SPACE", 0x053f1): (165, "ModuleInfoEntryMap"),
  ("RO_SPACE", 0x05441): (166, "ModuleMap"),
  ("RO_SPACE", 0x05491): (167, "ObjectTemplateInfoMap"),
  ("RO_SPACE", 0x054e1): (168, "PromiseCapabilityMap"),
  ("RO_SPACE", 0x05531): (169, "PromiseReactionMap"),
  ("RO_SPACE", 0x05581): (170, "PrototypeInfoMap"),
  ("RO_SPACE", 0x055d1): (171, "ScriptMap"),
  ("RO_SPACE", 0x05621): (172, "StackFrameInfoMap"),
  ("RO_SPACE", 0x05671): (174, "Tuple3Map"),
  ("RO_SPACE", 0x056c1): (176, "WasmDebugInfoMap"),
  ("RO_SPACE", 0x05711): (177, "WasmExceptionTagMap"),
  ("RO_SPACE", 0x05761): (178, "WasmExportedFunctionDataMap"),
  ("RO_SPACE", 0x057b1): (179, "CallableTaskMap"),
  ("RO_SPACE", 0x05801): (180, "CallbackTaskMap"),
  ("RO_SPACE", 0x05851): (181, "PromiseFulfillReactionJobTaskMap"),
  ("RO_SPACE", 0x058a1): (182, "PromiseRejectReactionJobTaskMap"),
  ("RO_SPACE", 0x058f1): (183, "PromiseResolveThenableJobTaskMap"),
  ("RO_SPACE", 0x05941): (184, "WeakFactoryCleanupJobTaskMap"),
  ("RO_SPACE", 0x05991): (185, "AllocationSiteWithWeakNextMap"),
  ("RO_SPACE", 0x059e1): (185, "AllocationSiteWithoutWeakNextMap"),
  ("RO_SPACE", 0x05a31): (219, "LoadHandler1Map"),
  ("RO_SPACE", 0x05a81): (219, "LoadHandler2Map"),
  ("RO_SPACE", 0x05ad1): (219, "LoadHandler3Map"),
  ("RO_SPACE", 0x05b21): (227, "StoreHandler0Map"),
  ("RO_SPACE", 0x05b71): (227, "StoreHandler1Map"),
  ("RO_SPACE", 0x05bc1): (227, "StoreHandler2Map"),
  ("RO_SPACE", 0x05c11): (227, "StoreHandler3Map"),
  ("MAP_SPACE", 0x00139): (1057, "ExternalMap"),
  ("MAP_SPACE", 0x00189): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("RO_SPACE", 0x001d9): "NullValue",
  ("RO_SPACE", 0x00259): "EmptyDescriptorArray",
  ("RO_SPACE", 0x002c1): "EmptyWeakFixedArray",
  ("RO_SPACE", 0x003c1): "UninitializedValue",
  ("RO_SPACE", 0x004d1): "UndefinedValue",
  ("RO_SPACE", 0x00551): "NanValue",
  ("RO_SPACE", 0x005b1): "TheHoleValue",
  ("RO_SPACE", 0x00649): "HoleNanValue",
  ("RO_SPACE", 0x00659): "TrueValue",
  ("RO_SPACE", 0x00709): "FalseValue",
  ("RO_SPACE", 0x00751): "empty_string",
  ("RO_SPACE", 0x00c11): "EmptyScopeInfo",
  ("RO_SPACE", 0x00c21): "EmptyFixedArray",
  ("RO_SPACE", 0x00c31): "ArgumentsMarker",
  ("RO_SPACE", 0x00cd1): "Exception",
  ("RO_SPACE", 0x00d71): "TerminationException",
  ("RO_SPACE", 0x00e19): "OptimizedOut",
  ("RO_SPACE", 0x00eb9): "StaleRegister",
  ("RO_SPACE", 0x027b9): "EmptyEnumCache",
  ("RO_SPACE", 0x02821): "EmptyPropertyArray",
  ("RO_SPACE", 0x02831): "EmptyByteArray",
  ("RO_SPACE", 0x02841): "EmptyObjectBoilerplateDescription",
  ("RO_SPACE", 0x02859): "EmptyArrayBoilerplateDescription",
  ("RO_SPACE", 0x028c1): "EmptyFixedUint8Array",
  ("RO_SPACE", 0x028e1): "EmptyFixedInt8Array",
  ("RO_SPACE", 0x02901): "EmptyFixedUint16Array",
  ("RO_SPACE", 0x02921): "EmptyFixedInt16Array",
  ("RO_SPACE", 0x02941): "EmptyFixedUint32Array",
  ("RO_SPACE", 0x02961): "EmptyFixedInt32Array",
  ("RO_SPACE", 0x02981): "EmptyFixedFloat32Array",
  ("RO_SPACE", 0x029a1): "EmptyFixedFloat64Array",
  ("RO_SPACE", 0x029c1): "EmptyFixedUint8ClampedArray",
  ("RO_SPACE", 0x029e1): "EmptyFixedBigUint64Array",
  ("RO_SPACE", 0x02a01): "EmptyFixedBigInt64Array",
  ("RO_SPACE", 0x02a21): "EmptySloppyArgumentsElements",
  ("RO_SPACE", 0x02a41): "EmptySlowElementDictionary",
  ("RO_SPACE", 0x02a89): "EmptyOrderedHashMap",
  ("RO_SPACE", 0x02ab1): "EmptyOrderedHashSet",
  ("RO_SPACE", 0x02ad9): "EmptyFeedbackMetadata",
  ("RO_SPACE", 0x02ae9): "EmptyPropertyCell",
  ("RO_SPACE", 0x02b11): "EmptyPropertyDictionary",
  ("RO_SPACE", 0x02b61): "NoOpInterceptorInfo",
  ("RO_SPACE", 0x02c01): "EmptyWeakArrayList",
  ("RO_SPACE", 0x02c19): "InfinityValue",
  ("RO_SPACE", 0x02c29): "MinusZeroValue",
  ("RO_SPACE", 0x02c39): "MinusInfinityValue",
  ("RO_SPACE", 0x02c49): "SelfReferenceMarker",
  ("RO_SPACE", 0x02ca1): "OffHeapTrampolineRelocationInfo",
  ("RO_SPACE", 0x02cb9): "HashSeed",
  ("OLD_SPACE", 0x00139): "ArgumentsIteratorAccessor",
  ("OLD_SPACE", 0x001a9): "ArrayLengthAccessor",
  ("OLD_SPACE", 0x00219): "BoundFunctionLengthAccessor",
  ("OLD_SPACE", 0x00289): "BoundFunctionNameAccessor",
  ("OLD_SPACE", 0x002f9): "ErrorStackAccessor",
  ("OLD_SPACE", 0x00369): "FunctionArgumentsAccessor",
  ("OLD_SPACE", 0x003d9): "FunctionCallerAccessor",
  ("OLD_SPACE", 0x00449): "FunctionNameAccessor",
  ("OLD_SPACE", 0x004b9): "FunctionLengthAccessor",
  ("OLD_SPACE", 0x00529): "FunctionPrototypeAccessor",
  ("OLD_SPACE", 0x00599): "StringLengthAccessor",
  ("OLD_SPACE", 0x00609): "InvalidPrototypeValidityCell",
  ("OLD_SPACE", 0x00619): "EmptyScript",
  ("OLD_SPACE", 0x00699): "ManyClosuresCell",
  ("OLD_SPACE", 0x006a9): "NoFeedbackCell",
  ("OLD_SPACE", 0x006b9): "ArrayConstructorProtector",
  ("OLD_SPACE", 0x006c9): "NoElementsProtector",
  ("OLD_SPACE", 0x006f1): "IsConcatSpreadableProtector",
  ("OLD_SPACE", 0x00701): "ArraySpeciesProtector",
  ("OLD_SPACE", 0x00729): "TypedArraySpeciesProtector",
  ("OLD_SPACE", 0x00751): "RegExpSpeciesProtector",
  ("OLD_SPACE", 0x00779): "PromiseSpeciesProtector",
  ("OLD_SPACE", 0x007a1): "StringLengthProtector",
  ("OLD_SPACE", 0x007b1): "ArrayIteratorProtector",
  ("OLD_SPACE", 0x007d9): "ArrayBufferDetachingProtector",
  ("OLD_SPACE", 0x00801): "PromiseHookProtector",
  ("OLD_SPACE", 0x00829): "PromiseResolveProtector",
  ("OLD_SPACE", 0x00839): "MapIteratorProtector",
  ("OLD_SPACE", 0x00861): "PromiseThenProtector",
  ("OLD_SPACE", 0x00889): "SetIteratorProtector",
  ("OLD_SPACE", 0x008b1): "StringIteratorProtector",
  ("OLD_SPACE", 0x008d9): "SingleCharacterStringCache",
  ("OLD_SPACE", 0x010e9): "StringSplitCache",
  ("OLD_SPACE", 0x018f9): "RegExpMultipleCache",
  ("OLD_SPACE", 0x02109): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
