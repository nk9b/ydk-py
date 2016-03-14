


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IpIepPath_Enum' : _MetaInfoEnum('IpIepPath_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg',
        {
            'identifier':'IDENTIFIER',
            'name':'NAME',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg']),
    'IpIepHop_Enum' : _MetaInfoEnum('IpIepHop_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg',
        {
            'next-strict':'NEXT_STRICT',
            'next-loose':'NEXT_LOOSE',
            'exclude':'EXCLUDE',
            'exclude-srlg':'EXCLUDE_SRLG',
            'next-label':'NEXT_LABEL',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg']),
    'IpIepNum_Enum' : _MetaInfoEnum('IpIepNum_Enum', 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg',
        {
            'unnumbered':'UNNUMBERED',
            'numbered':'NUMBERED',
        }, 'Cisco-IOS-XR-ip-iep-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg']),
    'IpExplicitPaths.Paths.Path.Identifier.Hops.Hop' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier.Hops.Hop',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IpIepHop_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop_Enum', 
                [], [], 
                '''                Include or exclude this hop in the path
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ifindex value
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the hop
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('num-type', REFERENCE_ENUM_CLASS, 'IpIepNum_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum_Enum', 
                [], [], 
                '''                Number type Numbered or Unnumbered
                ''',
                'num_type',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path.Identifier.Hops' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier.Hops',
            False, 
            [
            _MetaInfoClassMember('hop', REFERENCE_LIST, 'Hop' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier.Hops.Hop', 
                [], [], 
                '''                Hop Information
                ''',
                'hop',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hops',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path.Identifier' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Identifier',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Path identifier
                ''',
                'id',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable the explicit path
                ''',
                'disable',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('hops', REFERENCE_CLASS, 'Hops' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier.Hops', 
                [], [], 
                '''                List of Hops
                ''',
                'hops',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'identifier',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path.Name.Hops.Hop' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name.Hops.Hop',
            False, 
            [
            _MetaInfoClassMember('index-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Index number
                ''',
                'index_number',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'IpIepHop_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop_Enum', 
                [], [], 
                '''                Include or exclude this hop in the path
                ''',
                'hop_type',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Ifindex value
                ''',
                'if_index',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the hop
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('num-type', REFERENCE_ENUM_CLASS, 'IpIepNum_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum_Enum', 
                [], [], 
                '''                Number type Numbered or Unnumbered
                ''',
                'num_type',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path.Name.Hops' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name.Hops',
            False, 
            [
            _MetaInfoClassMember('hop', REFERENCE_LIST, 'Hop' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name.Hops.Hop', 
                [], [], 
                '''                Hop Information
                ''',
                'hop',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'hops',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path.Name' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path.Name',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Path name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable the explicit path
                ''',
                'disable',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('hops', REFERENCE_CLASS, 'Hops' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name.Hops', 
                [], [], 
                '''                List of Hops
                ''',
                'hops',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths.Path' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'IpIepPath_Enum' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpIepPath_Enum', 
                [], [], 
                '''                Path type
                ''',
                'type',
                'Cisco-IOS-XR-ip-iep-cfg', True),
            _MetaInfoClassMember('identifier', REFERENCE_LIST, 'Identifier' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Identifier', 
                [], [], 
                '''                identifier
                ''',
                'identifier',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            _MetaInfoClassMember('name', REFERENCE_LIST, 'Name' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path.Name', 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths.Paths' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths.Path', 
                [], [], 
                '''                Config data for a specific explicit path
                ''',
                'path',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
    'IpExplicitPaths' : {
        'meta_info' : _MetaInfoClass('IpExplicitPaths',
            False, 
            [
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg', 'IpExplicitPaths.Paths', 
                [], [], 
                '''                A list of explicit paths
                ''',
                'paths',
                'Cisco-IOS-XR-ip-iep-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iep-cfg',
            'ip-explicit-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iep-cfg'],
        'ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg'
        ),
    },
}
_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops.Hop']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Name.Hops.Hop']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths.Path']['meta_info']
_meta_table['IpExplicitPaths.Paths.Path']['meta_info'].parent =_meta_table['IpExplicitPaths.Paths']['meta_info']
_meta_table['IpExplicitPaths.Paths']['meta_info'].parent =_meta_table['IpExplicitPaths']['meta_info']