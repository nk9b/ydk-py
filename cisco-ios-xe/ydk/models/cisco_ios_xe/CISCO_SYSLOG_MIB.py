""" CISCO_SYSLOG_MIB 

The MIB module to describe and store the system
messages generated by the IOS and any other
OS which supports syslogs.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SyslogSeverity(Enum):
    """
    SyslogSeverity (Enum Class)

    The severity of a syslog message.  The enumeration

    values are equal to the values that syslog uses + 1.

    For example, with syslog, emergency=0.

     'emergency' \: system is unusable

     'alert'     \: action must be taken immediately

     'critical'  \: critical conditions

     'error'     \: error conditions

     'warning'   \: warning conditions

     'notice'    \: normal but significant condition

     'informational'\: informational messages 

     'debug'        \: debug\-level messages.

    .. data:: emergency = 1

    .. data:: alert = 2

    .. data:: critical = 3

    .. data:: error = 4

    .. data:: warning = 5

    .. data:: notice = 6

    .. data:: info = 7

    .. data:: debug = 8

    """

    emergency = Enum.YLeaf(1, "emergency")

    alert = Enum.YLeaf(2, "alert")

    critical = Enum.YLeaf(3, "critical")

    error = Enum.YLeaf(4, "error")

    warning = Enum.YLeaf(5, "warning")

    notice = Enum.YLeaf(6, "notice")

    info = Enum.YLeaf(7, "info")

    debug = Enum.YLeaf(8, "debug")



class CISCOSYSLOGMIB(Entity):
    """
    
    
    .. attribute:: clogbasic
    
    	
    	**type**\:  :py:class:`Clogbasic <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Clogbasic>`
    
    .. attribute:: cloghistory
    
    	
    	**type**\:  :py:class:`Cloghistory <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Cloghistory>`
    
    .. attribute:: clogserver
    
    	
    	**type**\:  :py:class:`Clogserver <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Clogserver>`
    
    .. attribute:: cloghistorytable
    
    	A table of syslog messages generated by this device. All 'interesting' syslog messages (i.e. severity <= clogMaxSeverity) are entered into this table
    	**type**\:  :py:class:`Cloghistorytable <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Cloghistorytable>`
    
    .. attribute:: clogserverconfigtable
    
    	This table contains entries that allow application to configure syslog servers for the system.  The maximum number of entries that can be created for this table is limited by the object clogMaxServers
    	**type**\:  :py:class:`Clogserverconfigtable <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Clogserverconfigtable>`
    
    

    """

    _prefix = 'CISCO-SYSLOG-MIB'
    _revision = '2005-12-03'

    def __init__(self):
        super(CISCOSYSLOGMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SYSLOG-MIB"
        self.yang_parent_name = "CISCO-SYSLOG-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("clogBasic", ("clogbasic", CISCOSYSLOGMIB.Clogbasic)), ("clogHistory", ("cloghistory", CISCOSYSLOGMIB.Cloghistory)), ("clogServer", ("clogserver", CISCOSYSLOGMIB.Clogserver)), ("clogHistoryTable", ("cloghistorytable", CISCOSYSLOGMIB.Cloghistorytable)), ("clogServerConfigTable", ("clogserverconfigtable", CISCOSYSLOGMIB.Clogserverconfigtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.clogbasic = CISCOSYSLOGMIB.Clogbasic()
        self.clogbasic.parent = self
        self._children_name_map["clogbasic"] = "clogBasic"
        self._children_yang_names.add("clogBasic")

        self.cloghistory = CISCOSYSLOGMIB.Cloghistory()
        self.cloghistory.parent = self
        self._children_name_map["cloghistory"] = "clogHistory"
        self._children_yang_names.add("clogHistory")

        self.clogserver = CISCOSYSLOGMIB.Clogserver()
        self.clogserver.parent = self
        self._children_name_map["clogserver"] = "clogServer"
        self._children_yang_names.add("clogServer")

        self.cloghistorytable = CISCOSYSLOGMIB.Cloghistorytable()
        self.cloghistorytable.parent = self
        self._children_name_map["cloghistorytable"] = "clogHistoryTable"
        self._children_yang_names.add("clogHistoryTable")

        self.clogserverconfigtable = CISCOSYSLOGMIB.Clogserverconfigtable()
        self.clogserverconfigtable.parent = self
        self._children_name_map["clogserverconfigtable"] = "clogServerConfigTable"
        self._children_yang_names.add("clogServerConfigTable")
        self._segment_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB"


    class Clogbasic(Entity):
        """
        
        
        .. attribute:: clognotificationssent
        
        	The number of clogMessageGenerated notifications that have been sent. This number may include notifications that were prevented from being transmitted due to reasons such as resource limitations and/or non\-connectivity.  If one is receiving notifications, one can periodically poll this object to determine if any notifications were missed.  If so, a poll of the clogHistoryTable might be appropriate
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: notifications
        
        .. attribute:: clognotificationsenabled
        
        	Indicates whether clogMessageGenerated notifications will or will not be sent when a syslog message is generated by the device.  Disabling notifications does not prevent syslog messages from being added to the clogHistoryTable
        	**type**\: bool
        
        .. attribute:: clogmaxseverity
        
        	Indicates which syslog severity levels will be processed.  Any syslog message with a severity value greater than this value will be ignored by the agent. note\: severity numeric values increase as their severity decreases, e.g. 'error' is more severe than 'debug'
        	**type**\:  :py:class:`SyslogSeverity <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.SyslogSeverity>`
        
        .. attribute:: clogmsgignores
        
        	The number of syslog messages which were ignored.  A message will be ignored if it has a severity value greater than clogMaxSeverity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: messages
        
        .. attribute:: clogmsgdrops
        
        	The number of syslog messages which could not be processed due to lack of system resources. Most likely this will occur at the same time that syslog messages are generated to indicate this lack of resources.  Increases in this object's value may serve as an indication that system resource levels should be examined via other mib objects.  A message that is dropped will not appear in the history table and no notification will be sent for this message
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: messages
        
        .. attribute:: clogoriginidtype
        
        	This object identifies the type of value that will be contained in clogOriginID object.  The possible value(s) are\:    'none'       \: do not send origin identifier in                    syslog messages.    'other'      \: type that is not identified by other                    values specified in this object.    'hostName'   \: Send hostname of the system in syslog                   messages.    'ipv4Address'\: Send IP address of the sending interface.    'contextName'\: Send context name of the security device.    'userDefined'\: Send user configured string in                   syslog message.     The value 'other' and 'none' can not be set but    can only be read
        	**type**\:  :py:class:`Clogoriginidtype <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Clogbasic.Clogoriginidtype>`
        
        .. attribute:: clogoriginid
        
        	This object is used for configuring the origin identifier for the syslog messages.  The origin identifier is useful for identifying  the source of system logging messages in cases  syslog messages from multiple devices are sent  to a single syslog host. The origin identifier is added to the beginning of all system logging (syslog) messages sent to remote  hosts.  The type of the identifier is specified by clogOriginIDType object.  This object can be written by the SNMP manager only when clogOriginIDType is set to 'userDefined'.  For following value(s) of clogOriginIDType, this object can not be set; the value of this object is derived by the system in these cases\:    'contextName'     'ipv4Address'    'hostName'    'other'         'none'       This object contains the context name of the device, when clogOriginIDType is  set to 'contextName'.  This object contains IPv4 address (in dotted decimal notation) of the sending  interface when clogOriginIDType is set to 'ipv4Address'.  This object contains hostname of the system when clogOriginIDType is set to 'hostName'.  This object will contain zero length octet string when clogOriginIDType is either 'none' or 'other'
        	**type**\: str
        
        

        """

        _prefix = 'CISCO-SYSLOG-MIB'
        _revision = '2005-12-03'

        def __init__(self):
            super(CISCOSYSLOGMIB.Clogbasic, self).__init__()

            self.yang_name = "clogBasic"
            self.yang_parent_name = "CISCO-SYSLOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('clognotificationssent', YLeaf(YType.uint32, 'clogNotificationsSent')),
                ('clognotificationsenabled', YLeaf(YType.boolean, 'clogNotificationsEnabled')),
                ('clogmaxseverity', YLeaf(YType.enumeration, 'clogMaxSeverity')),
                ('clogmsgignores', YLeaf(YType.uint32, 'clogMsgIgnores')),
                ('clogmsgdrops', YLeaf(YType.uint32, 'clogMsgDrops')),
                ('clogoriginidtype', YLeaf(YType.enumeration, 'clogOriginIDType')),
                ('clogoriginid', YLeaf(YType.str, 'clogOriginID')),
            ])
            self.clognotificationssent = None
            self.clognotificationsenabled = None
            self.clogmaxseverity = None
            self.clogmsgignores = None
            self.clogmsgdrops = None
            self.clogoriginidtype = None
            self.clogoriginid = None
            self._segment_path = lambda: "clogBasic"
            self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSYSLOGMIB.Clogbasic, ['clognotificationssent', 'clognotificationsenabled', 'clogmaxseverity', 'clogmsgignores', 'clogmsgdrops', 'clogoriginidtype', 'clogoriginid'], name, value)

        class Clogoriginidtype(Enum):
            """
            Clogoriginidtype (Enum Class)

            This object identifies the type of value that

            will be contained in clogOriginID object.

            The possible value(s) are\:

               'none'       \: do not send origin identifier in 

                              syslog messages.

               'other'      \: type that is not identified by other 

                              values specified in this object.

               'hostName'   \: Send hostname of the system in syslog

                              messages.

               'ipv4Address'\: Send IP address of the sending interface.

               'contextName'\: Send context name of the security device.

               'userDefined'\: Send user configured string in

                              syslog message.

               The value 'other' and 'none' can not be set but

               can only be read.

            .. data:: none = 1

            .. data:: other = 2

            .. data:: hostName = 3

            .. data:: ipv4Address = 4

            .. data:: contextName = 5

            .. data:: userDefined = 6

            """

            none = Enum.YLeaf(1, "none")

            other = Enum.YLeaf(2, "other")

            hostName = Enum.YLeaf(3, "hostName")

            ipv4Address = Enum.YLeaf(4, "ipv4Address")

            contextName = Enum.YLeaf(5, "contextName")

            userDefined = Enum.YLeaf(6, "userDefined")



    class Cloghistory(Entity):
        """
        
        
        .. attribute:: cloghisttablemaxlength
        
        	The upper limit on the number of entries that the clogHistoryTable may contain.  A value of 0 will prevent any history from being retained. When this table is full, the oldest entry will be deleted and a new one will be created
        	**type**\: int
        
        	**range:** 0..500
        
        	**units**\: entries
        
        .. attribute:: cloghistmsgsflushed
        
        	The number of entries that have been removed from the clogHistoryTable in order to make room for new entries. This object can be utilized to determine whether your polling frequency on the history table is fast enough and/or the size of your history table is large enough such that you are not missing messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: messages
        
        

        """

        _prefix = 'CISCO-SYSLOG-MIB'
        _revision = '2005-12-03'

        def __init__(self):
            super(CISCOSYSLOGMIB.Cloghistory, self).__init__()

            self.yang_name = "clogHistory"
            self.yang_parent_name = "CISCO-SYSLOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cloghisttablemaxlength', YLeaf(YType.int32, 'clogHistTableMaxLength')),
                ('cloghistmsgsflushed', YLeaf(YType.uint32, 'clogHistMsgsFlushed')),
            ])
            self.cloghisttablemaxlength = None
            self.cloghistmsgsflushed = None
            self._segment_path = lambda: "clogHistory"
            self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSYSLOGMIB.Cloghistory, ['cloghisttablemaxlength', 'cloghistmsgsflushed'], name, value)


    class Clogserver(Entity):
        """
        
        
        .. attribute:: clogmaxservers
        
        	The maximum number of syslog servers that can be configured for the system in clogServerConfigTable.  A value of zero for this object indicates there is no specified limit for the system and is only dictated by system resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-SYSLOG-MIB'
        _revision = '2005-12-03'

        def __init__(self):
            super(CISCOSYSLOGMIB.Clogserver, self).__init__()

            self.yang_name = "clogServer"
            self.yang_parent_name = "CISCO-SYSLOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('clogmaxservers', YLeaf(YType.uint32, 'clogMaxServers')),
            ])
            self.clogmaxservers = None
            self._segment_path = lambda: "clogServer"
            self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSYSLOGMIB.Clogserver, ['clogmaxservers'], name, value)


    class Cloghistorytable(Entity):
        """
        A table of syslog messages generated by this device.
        All 'interesting' syslog messages (i.e. severity <=
        clogMaxSeverity) are entered into this table.
        
        .. attribute:: cloghistoryentry
        
        	A syslog message that was previously generated by this device. Each entry is indexed by a message index
        	**type**\: list of  		 :py:class:`Cloghistoryentry <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Cloghistorytable.Cloghistoryentry>`
        
        

        """

        _prefix = 'CISCO-SYSLOG-MIB'
        _revision = '2005-12-03'

        def __init__(self):
            super(CISCOSYSLOGMIB.Cloghistorytable, self).__init__()

            self.yang_name = "clogHistoryTable"
            self.yang_parent_name = "CISCO-SYSLOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("clogHistoryEntry", ("cloghistoryentry", CISCOSYSLOGMIB.Cloghistorytable.Cloghistoryentry))])
            self._leafs = OrderedDict()

            self.cloghistoryentry = YList(self)
            self._segment_path = lambda: "clogHistoryTable"
            self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSYSLOGMIB.Cloghistorytable, [], name, value)


        class Cloghistoryentry(Entity):
            """
            A syslog message that was previously generated by this
            device. Each entry is indexed by a message index.
            
            .. attribute:: cloghistindex  (key)
            
            	A monotonically increasing integer for the sole purpose of indexing messages.  When it reaches the maximum value the agent flushes the table and wraps the value back to 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cloghistfacility
            
            	Name of the facility that generated this message. For example\: 'SYS'
            	**type**\: str
            
            	**length:** 1..20
            
            .. attribute:: cloghistseverity
            
            	The severity of the message
            	**type**\:  :py:class:`SyslogSeverity <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.SyslogSeverity>`
            
            .. attribute:: cloghistmsgname
            
            	A textual identification for the message type. A facility name in conjunction with a message name uniquely identifies a message type
            	**type**\: str
            
            	**length:** 1..30
            
            .. attribute:: cloghistmsgtext
            
            	The text of the message.  If the text of the message exceeds 255 bytes, the message will be truncated to 254 bytes and a '\*' character will be appended \- indicating that the message has been truncated
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cloghisttimestamp
            
            	The value of sysUpTime when this message was generated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-SYSLOG-MIB'
            _revision = '2005-12-03'

            def __init__(self):
                super(CISCOSYSLOGMIB.Cloghistorytable.Cloghistoryentry, self).__init__()

                self.yang_name = "clogHistoryEntry"
                self.yang_parent_name = "clogHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cloghistindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cloghistindex', YLeaf(YType.int32, 'clogHistIndex')),
                    ('cloghistfacility', YLeaf(YType.str, 'clogHistFacility')),
                    ('cloghistseverity', YLeaf(YType.enumeration, 'clogHistSeverity')),
                    ('cloghistmsgname', YLeaf(YType.str, 'clogHistMsgName')),
                    ('cloghistmsgtext', YLeaf(YType.str, 'clogHistMsgText')),
                    ('cloghisttimestamp', YLeaf(YType.uint32, 'clogHistTimestamp')),
                ])
                self.cloghistindex = None
                self.cloghistfacility = None
                self.cloghistseverity = None
                self.cloghistmsgname = None
                self.cloghistmsgtext = None
                self.cloghisttimestamp = None
                self._segment_path = lambda: "clogHistoryEntry" + "[clogHistIndex='" + str(self.cloghistindex) + "']"
                self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/clogHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSYSLOGMIB.Cloghistorytable.Cloghistoryentry, ['cloghistindex', 'cloghistfacility', 'cloghistseverity', 'cloghistmsgname', 'cloghistmsgtext', 'cloghisttimestamp'], name, value)


    class Clogserverconfigtable(Entity):
        """
        This table contains entries that allow application
        to configure syslog servers for the system.
        
        The maximum number of entries that can be created
        for this table is limited by the object
        clogMaxServers.
        
        .. attribute:: clogserverconfigentry
        
        	An entry containing information about syslog servers configured for the system
        	**type**\: list of  		 :py:class:`Clogserverconfigentry <ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB.CISCOSYSLOGMIB.Clogserverconfigtable.Clogserverconfigentry>`
        
        

        """

        _prefix = 'CISCO-SYSLOG-MIB'
        _revision = '2005-12-03'

        def __init__(self):
            super(CISCOSYSLOGMIB.Clogserverconfigtable, self).__init__()

            self.yang_name = "clogServerConfigTable"
            self.yang_parent_name = "CISCO-SYSLOG-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("clogServerConfigEntry", ("clogserverconfigentry", CISCOSYSLOGMIB.Clogserverconfigtable.Clogserverconfigentry))])
            self._leafs = OrderedDict()

            self.clogserverconfigentry = YList(self)
            self._segment_path = lambda: "clogServerConfigTable"
            self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSYSLOGMIB.Clogserverconfigtable, [], name, value)


        class Clogserverconfigentry(Entity):
            """
            An entry containing information about syslog servers
            configured for the system.
            
            .. attribute:: clogserveraddrtype  (key)
            
            	The type of Internet address of this syslog server
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: clogserveraddr  (key)
            
            	The Internet address of this syslog server. The type of this address is determined by the value of the clogServerAddrType object
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: clogserverstatus
            
            	The status object used to manage rows in this table.  A row may only be created by setting this object to 'createAndGo'.  A row may only be deleted by setting this object to 'destroy'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-SYSLOG-MIB'
            _revision = '2005-12-03'

            def __init__(self):
                super(CISCOSYSLOGMIB.Clogserverconfigtable.Clogserverconfigentry, self).__init__()

                self.yang_name = "clogServerConfigEntry"
                self.yang_parent_name = "clogServerConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['clogserveraddrtype','clogserveraddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clogserveraddrtype', YLeaf(YType.enumeration, 'clogServerAddrType')),
                    ('clogserveraddr', YLeaf(YType.str, 'clogServerAddr')),
                    ('clogserverstatus', YLeaf(YType.enumeration, 'clogServerStatus')),
                ])
                self.clogserveraddrtype = None
                self.clogserveraddr = None
                self.clogserverstatus = None
                self._segment_path = lambda: "clogServerConfigEntry" + "[clogServerAddrType='" + str(self.clogserveraddrtype) + "']" + "[clogServerAddr='" + str(self.clogserveraddr) + "']"
                self._absolute_path = lambda: "CISCO-SYSLOG-MIB:CISCO-SYSLOG-MIB/clogServerConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSYSLOGMIB.Clogserverconfigtable.Clogserverconfigentry, ['clogserveraddrtype', 'clogserveraddr', 'clogserverstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOSYSLOGMIB()
        return self._top_entity

