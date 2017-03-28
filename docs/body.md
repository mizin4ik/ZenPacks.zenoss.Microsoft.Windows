<style>
img.thumbnail {
    clear: right;
    float: right;
    margin: 0 0 10px 10px;
    padding: 0px;
    width: 320px;
    font-size: small;
    font-style: italic;
}
br.clear {
    clear: right;
}
dd {
    font-size: smaller;
}
</style>

Video
-----

<p><iframe allowfullscreen="" class="media-element file-default" data-fid="15551" data-media-element="1" frameborder="0" height="360" src="https://www.youtube.com/embed/kP28F_aQ77E?feature=oembed" width="640"></iframe></p><p><iframe allowfullscreen="" class="media-element file-default" data-fid="15556" data-media-element="1" frameborder="0" height="360" src="https://www.youtube.com/embed/IIa5uiYaJj4?feature=oembed" width="640"></iframe></p>

Features
--------

The features added by this ZenPack can be summarized as follows. They
are each detailed further below.

-   Initial discovery and periodic remodeling of relevant components.
-   Performance monitoring.
-   Event management.
-   Custom commands.
-   Service monitoring.

### Discovery

The following components will be automatically discovered through the
Windows server address, username and password you provide. The
properties and relationships will be periodically updated by modeling.

[![][Windows_device.png]][Windows_device.png]

[![][Windows_filesystem.png]][Windows_filesystem.png]

Server (Device)
:   **Attributes:** Name, Contact, Description, Serial
    Number, Tag, Hardware Model, Physical Memory, Total Virtual Memory,
    Operating System, Cluster
:   **Relationships:** File Systems, Hard Disks, Processes, IP Services,
    CPUs, Interfaces, Windows Services, HyperV, SQL Server Instances,
    IIS Sites

Cluster (Device)
:   **Attributes:** Name, Contact, Description, Physical
    Memory, Total Virtual Memory, Operating System, Member Servers
:   **Relationships:** File Systems, Hard Disks, Processes, IP Services,
    CPUs, Interfaces, Windows Services, HyperV, SQL Server Instances,
    IIS Sites, Cluster Services, Cluster Resources, Cluster Networks,
    Cluster Disks, Cluster Interfaces, Cluster Nodes

Processors
:   **Attributes:** Name, Description, Model, Socket, Cores,
    Threads, Clock Speed, External Speed, Voltage, L1 Cache Size, L2 Cache
    Size and Speed, L3 Cache Size and Speed
:   **Relationships:** Device

Hard Disks
:   **Attributes:** Name, Size, Number of Partitions, Disk Ids,
    Free Space, Capabilities
:   **Relationships:** Device, File Systems

File Systems
:   **Attributes:** Mount Point, Status, Storage Device, Type,
    Block Size, Total Blocks, Total Bytes, Maximum Name Length
:   **Relationships:** Device, Hard Disks

Interfaces
:   **Attributes:** Name, Description, MAC Address, MTU, Speed,
    Duplex, Type, Administrative Status, Operational Status, IP Addresses
:   **Relationships:** Device

[[File:windows\_interfaces.png|thumb|320px|Interfaces]]

Network Routes
:   **Attributes:** Destination, Next Hop, Interface,
    Protocol, Type
:   **Relationships:** Device

Process Sets
:   **Attributes:** Name, Recent Matches, Process Class
:   **Relationships:** Device

Software
:   **Attributes:** Name, Vendor, Installation Date
:   **Relationships:** Device

Services
:   **Attributes:** Name, Display Name, Start Mode, Account
:   **Relationships:** Device

Cluster Services
:   **Attributes:** Name, Core Group, Owner Node, State,
    Description, Priority
:   **Relationships:** Cluster Resources

Cluster Resources
:   **Attributes:** Name, Owner Node, Description, Owner
    Group, State
:   **Relationships:** Cluster Service

Cluster Nodes
:   **Attributes:** Name, Assigned Vote, Current Vote, State :
:   **Relationships:** Cluster Disks, Cluster Interfaces

Cluster Networks
:   **Attributes:** Name, Description, State

Cluster Disks
:   **Attributes:** Name, Owner Node, Volume Path, Disk Number,
    Partition Number, Capacity, Free Space, State
:   **Relationships:** Cluster Nodes

Cluster Interfaces
:   **Attributes:** Name, Owner Node, Network, IP
    Addresses, Adapter, State
:   **Relationships:** Cluster Nodes

IIS Sites
:   **Attributes:** Name, Status, App Pool
:   **Relationships:** Device

SQL Server Instances
:   **Attributes:** Name : Relationships: SQL Server databases
:   **Relationships:** Device

SQL Server Databases
:   **Attributes:** Name, Version, Owner, Last Backup,
    Last Log Backup, Accessible, Collation, Creation Date, Default File
    Group, Primary File Path, Recovery Model, Is System Object
:   **Relationships:** SQL Server Instance, Device

SQL Server Backups
:   **Attributes:** Name, Device Type, Physical
    Allocation, Status
:   **Relationships:** SQL Server Instance

SQL Server Jobs
:   **Attributes:** Name, Job ID, Description, Enabled, Date
    Created, Username
:   **Relationships:** SQL Server Instance

<br class="clear">

### Performance Monitoring

Performance counters are collected using the PowerShell Get-Counter Cmdlet
within a remote shell (WinRS). The following metrics will be collected
every 5 minutes by default. Any other Windows Perfmon counters can also
be collected by adding them to the appropriate monitoring template.

Device
:   \Memory\Available bytes
:   \Memory\Committed Bytes
:   \Memory\Pages Input/sec
:   \Memory\Pages Output/sec
:   \Paging File(_Total)\% Usage
:   \Processor(_Total)\% Privileged Time
:   \Processor(_Total)\% Processor Time
:   \Processor(_Total)\% User Time
:   \System\System Up Time

File Systems
:   \LogicalDisk({$here/instance_name})\Disk Read Bytes/sec 
:   \LogicalDisk({$here/instance_name})% Disk Read Time
:   \LogicalDisk({$here/instance_name})\Disk Write Bytes/sec
:   \LogicalDisk({$here/instance_name})% Disk Write Time
:   \LogicalDisk({\$here/instance_name})\Free Megabytes

Hard Disks
:   \PhysicalDisk({$here/instance_name})\Disk Read Bytes/sec
:   \PhysicalDisk({$here/instance_name})% Disk Read Time
:   \PhysicalDisk({$here/instance_name})\Disk Write Bytes/sec
:   \PhysicalDisk({$here/instance_name})% Disk Write Time

Interfaces
:   \Network Interface(${here/instance_name})\Bytes Received/sec
:   \Network Interface(${here/instance\_name})\Bytes Sent/sec
:   \Network Interface(${here/instance_name})\Packets Received Errors
:   \Network Interface(${here/instance\_name})\Packets Received/sec
:   \Network Interface(${here/instance_name})\Packets Outbound Errors
:   \Network Interface(${here/instance\_name})\Packets Sent/sec

;Interfaces on Windows 2012
:   \Network Adapter(${here/instance_name})\Bytes Received/sec
:   \Network Adapter(${here/instance\_name})\Bytes Sent/sec
:   \Network Adapter(${here/instance_name})\Packets Received Errors
:   \Network Adapter(${here/instance\_name})\Packets Received/sec
:   \Network Adapter(${here/instance_name})\Packets Outbound Errors
:   \Network Adapter(${here/instance\_name})\Packets Sent/sec

Active Directory
:   \NTDS\DS Client Binds/sec
:   \NTDS\DS Directory Reads/sec
:   \NTDS\DS Directory Searches/sec
:   \NTDS\DS Directory Writes/sec
:   \NTDS\DS Monitor List Size
:   \NTDS\DS Name Cache hit rate
:   \NTDS\DS Notify Queue Size
:   \NTDS\DS Search sub-operations/sec
:   \NTDS\DS Server Binds/sec
:   \NTDS\DS Server Name Translations/sec
:   \NTDS\DS Threads in Use
:   \NTDS\KDC AS Requests
:   \NTDS\KDC TGS Requests
:   \NTDS\Kerberos Authentications
:   \NTDS\LDAP Active Threads
:   \NTDS\LDAP Bind Time
:   \NTDS\LDAP Client Sessions
:   \NTDS\LDAP Closed Connections/sec
:   \NTDS\LDAP New Connections/sec
:   \NTDS\LDAP New SSL Connections/sec
:   \NTDS\LDAP Searches/sec
:   \NTDS\LDAP Successful Binds/sec
:   \NTDS\LDAP UDP operations/sec
:   \NTDS\LDAP Writes/sec
:   \Security System-Wide Statistics\NTLM Authentications

Note: The Active Directory monitoring template will only be used when
the server has the Primary or Backup Domain Controller role.

Exchange 2007 & 2010 
:   \MSExchangeIS Mailbox(_Total)\Folder opens/sec
:   \MSExchangeIS Mailbox(_Total)\Local delivery rate 
:   \MSExchangeIS Mailbox(_Total)\Message Opens/sec 
:   \MSExchangeIS\RPC Averaged Latency 
:   \MSExchangeIS\RPC Operations/sec
:   \MSExchangeIS\RPC Requests 
:   \MSExchangeTransport Queues(_Total)\Active Mailbox Delivery Queue Length
:   \MSExchangeTransport SmtpSend(_Total)\Messages Sent/sec

Exchange 2013 
:   \MSExchangeIS Store(_Total)\Folders opened/sec 
:   \MSExchangeIS Store(_Total)\Messages Delivered/sec 
:   \MSExchangeIS Store(_Total)\Messages opened/sec 
:   \MSExchange Store Interface(_Total)\RPC Latency average (msec) 
:   \MSExchange Store Interface(_Total)\RPC Requests sent/sec 
:   \MSExchange Store Interface(_Total)\RPC Requests sent 
:   \MSExchangeTransport Queues(_Total)\Active Mailbox Delivery Queue Length
:   \MSExchange Delivery SmtpSend(_Total)\Messages Sent/sec

Note: If monitoring Exchange with a non-administrator user, the user
must be a member of the Active Directory group "Exchange View-Only
Administrators" for pre-2010 Exchange installations or "View Only
Organization Management" for 2010 and later installations.


Note: IIS Management Scripts and Tools needs to be installed on the
server side in order to model and monitor IIS sites. This is done
through the Add Roles and Features tool on the Windows Server under Web
Server -> Management Tools -> IIS Management Scripts and Tools.

IIS
:   \Web Service(_Total)\Bytes Received/sec
:   \Web Service(_Total)\Bytes Sent/sec
:   \Web Service(_Total)\CGI Requests/sec
:   \Web Service(_Total)\Connection Attempts/sec
:   \Web Service(_Total)\Copy Requests/sec
:   \Web Service(_Total)\Delete Requests/sec
:   \Web Service(_Total)\Files Received/sec
:   \Web Service(_Total)\Files Sent/sec
:   \Web Service(_Total)\Get Requests/sec
:   \Web Service(_Total)\Head Requests/sec
:   \Web Service(_Total)\ISAPI Extension Requests/sec
:   \Web Service(_Total)\Lock Requests/sec
:   \Web Service(_Total)\Mkcol Requests/sec
:   \Web Service(_Total)\Move Requests/sec
:   \Web Service(_Total)\Options Requests/sec
:   \Web Service(_Total)\Other Request Methods/sec
:   \Web Service(_Total)\Post Requests/sec
:   \Web Service(_Total)\Propfind Requests/sec
:   \Web Service(_Total)\Proppatch Requests/sec
:   \Web Service(_Total)\Put Requests/sec
:   \Web Service(_Total)\Search Requests/sec
:   \Web Service(_Total)\Trace Requests/sec
:   \Web Service(_Total)\Unlock Requests/sec

IIS Sites 
:   \Web Service(${here/sitename})\Bytes Received/sec
:   \Web Service(${here/sitename})\Bytes Sent/sec
:   \Web Service(${here/sitename})\CGI Requests/sec
:   \Web Service(${here/sitename})\Connection Attempts/sec
:   \Web Service(${here/sitename})\Copy Requests/sec
:   \Web Service(${here/sitename})\Connection Attempts/sec
:   \Web Service(${here/sitename})\Delete Requests/sec
:   \Web Service(${here/sitename})\Files Received/sec
:   \Web Service(${here/sitename})\Files Sent/sec
:   \Web Service(${here/sitename})\Get Requests/sec
:   \Web Service(${here/sitename})\Head Requests/sec
:   \Web Service(${here/sitename})\ISAPI Extension Requests/sec 
:   \Web Service(${here/sitename})\Lock Requests/sec
:   \Web Service(${here/sitename})\Mkcol Requests/sec
:   \Web Service(${here/sitename})\Move Requests/sec
:   \Web Service(${here/sitename})\Options Requests/sec
:   \Web Service(${here/sitename})\Other Request Methods/sec
:   \Web Service(${here/sitename})\Post Requests/sec
:   \Web Service(${here/sitename})\Propfind Requests/sec
:   \Web Service(${here/sitename})\Proppatch Requests/sec
:   \Web Service(${here/sitename})\Put Requests/sec
:   \Web Service(${here/sitename})\Search Requests/sec
:   \Web Service(${here/sitename})\Trace Requests/sec
:   \Web Service(${here/sitename})\Unlock Requests/sec

Note: The IIS monitoring template will only be used when IIS is found
during modeling.

Note: The IISAdmin service must be running in order to collect IIS
data.

The following metrics are collected directly via WMI over WinRM.

Processes (Win32\_PerfFormattedData\_PerfProc\_Process) \*
PercentProcessorTime \* WorkingSet \* WorkingSetPrivate

<br class="clear">
Note: IIS 6 Management compatibility role no longer needs to be
installed on the server side in order to use the IIS Sites component.

SQL Server

The following performance counters are monitored via Powershell script per database:

:   \SQLServer:Databases(<dbname>)\Active Transactions
:   \SQLServer:Databases(<dbname>)\Backup/Restore Throughput/sec
:   \SQLServer:Databases(<dbname>)\Bulk Copy Rows/sec
:   \SQLServer:Databases(<dbname>)\Bulk Copy Throughput/sec
:   \SQLServer:Databases(<dbname>)\Cache Entries Count
:   \SQLServer:Databases(<dbname>)\Cache Entries Pinned Count
:   \SQLServer:Databases(<dbname>)\Cache Hit Ratio
:   \SQLServer:Databases(<dbname>)\Cache Hit Ratio Base
:   \SQLServer:Databases(<dbname>)\DBCC Logical Scan Bytes/sec
:   \SQLServer:Databases(<dbname>)\Data File(s) Size (KB)
:   \SQLServer:Databases(<dbname>)\Log Bytes Flushed/sec
:   \SQLServer:Databases(<dbname>)\Log Cache Hit Ratio
:   \SQLServer:Databases(<dbname>)\Log Cache Hit Ratio Base
:   \SQLServer:Databases(<dbname>)\Log Cache Reads/sec
:   \SQLServer:Databases(<dbname>)\Log File(s) Size (KB)
:   \SQLServer:Databases(<dbname>)\Log File(s) Used Size (KB)
:   \SQLServer:Databases(<dbname>)\Log Flush Wait Time
:   \SQLServer:Databases(<dbname>)\Log Flush Waits/sec
:   \SQLServer:Databases(<dbname>)\Log Flushes/sec
:   \SQLServer:Databases(<dbname>)\Log Growths
:   \SQLServer:Databases(<dbname>)\Percent Log Used
:   \SQLServer:Databases(<dbname>)\Log Shrinks
:   \SQLServer:Databases(<dbname>)\Log Truncations
:   \SQLServer:Databases(<dbname>)\Percent Log Used
:   \SQLServer:Databases(<dbname>)\Repl. Pending Xacts
:   \SQLServer:Databases(<dbname>)\Repl. Trans. Rate
:   \SQLServer:Databases(<dbname>)\Shrink Data Movement Bytes/sec
:   \SQLServer:Databases(<dbname>)\Transactions/sec

You can enable/disable any of these or change the cycle time by editing
the WinDatabase monitoring template.

Events will be sent depending upon one or more of the following statuses
of the database

:   AutoClosed: The database has been automatically closed.
:   EmergencyMode: The database is in emergency mode.
:   Inaccessible: The database is inaccessible. The server might be
    switched off or the network connection has been interrupted.
:   Normal: The database is available.
:   Offline: The database has been taken offline.
:   Recovering: The database is going through the recovery process.
:   RecoveryPending: The database is waiting to go through the recovery
    process.
:   Restoring: The database is going through the restore process.
:   Shutdown: The server on which the database resides has been shut
    down.
:   Standby: The database is in standby mode.
:   Suspect: The database has been marked as suspect. You will have to
    check the data, and the database might have to be restored from a
    backup.

:   'Normal' will send a clear event
:   'EmergencyMode' will send a critical event
:   'Inaccessible', 'Suspect', 'Shutdown' will send Error events
:   'RecoveryPending', 'Restoring', 'Recovering', 'Standby', 'AutoClosed',
    'Offline' will send Warning events

Status can be multiple items from above. For example, taking a database
offline will set the status to 'Offline, AutoClosed'.

The WinDBInstance monitoring template will monitor the status of a SQL
Server instance to inform the user if it is up or down.

The WinSQLJob monitoring template will monitor the status of a job on a
SQL Server instance to inform the user if it has succeeded, failed,
unknown, or other state.

Thresholds
----------

The following thresholds are set by default on the device monitoring
template and will trigger an alert if they are reached

-   CPU Utilization - 90% used
-   Paging File Usage - 95% used
-   Memory - 90% of total memory used

## Event Management

Events could be collected from the Windows
event log using a WinRM subscription. Events collected through this
mechanism will be timestamped based on the time they occurred within the
Windows event log. Not by the time at which they were collected.

To monitor EventLog events you should add to monitoring template with
"Windows EventLog" datasource. For the Event Log field put the name of
event log (e.g. "System") that you are interested in, and in the
EventQuery you could put the filter for events. The filter can be either
a PowerShell Where-Object block or XPath XML taken from a Windows Event
Viewer Custom View.

The default Get-WinEvent xml filter returns all events from the last
polling cycle. This list can be searched for specific Ids, severity, or
specific words in the message using PowerShell.

#### To target all events with a Warning or higher severity:

[![][CustomViewOptions.png]][CustomViewOptions.png]
For servers with pre-3.5 .NET installed: 

```{ $$_.EntryType -le [System.Diagnostics.EventLogEntryType]::Warning}```

`$$_` is the event object of EventLogEntry class.
`EntryType` is the attribute which determines severity, and
could contain one of the following values: `Error, Warning, Information, SuccessAudit,` or `FailureAudit`.
Also it has such attributes as `Message, MachineName, TimeGenerated, Source`. Full list you could find in the description of the [EventLogEntry](http://msdn.microsoft.com/en-us/library/vstudio/system.diagnostics.eventlogentry).

Note: This query is structured to look for "less than" although we are
looking for events "greater than" in severity. This is because the
EntryType is an enumeration where the integer values map to 1= Error, 2
= Warning, etc. This means lower numbers indicate higher severity.

For servers with .NET 3.5 & Later:

```{ $$_.Level -le [System.Diagnostics.Eventing.Reader.StandardEventLevel]::Warning}```

Or to look for a specific event id:

`{ $$_.Id -eq 4001}`

`$$_` is the event object of EventLogRecord class.
`Level` is the severity of the event. `Id` is the
property to compare for specific event ids. You can find the full
listing of properties at
https://technet.microsoft.com/en-us/library/Hh849682.aspx.

Note: This query is structured to look for "less than or equal" although
we are looking for events "greater than or equal" in severity. This is
because the Level is an enumeration where the integer values map to 1 =
Critical, 2 = Error, 3 = Warning, etc. This means lower numbers indicate
higher severity. The LogAlways event level evaluates to 0, which is less
than a Warning. These events are typically Informational and will
display if using the sample powershell query above. To work around this,
you could add ` -and $$_.Level -gt
[System.Diagnostics.Eventing.Reader.StandardEventLevel]::LogAlways`
into your query or use the xml option.

[![][CustomViewXML.png]][CustomViewXML.png] The full list of
event levels can be found in the description of the [Standard Event Level](http://msdn.microsoft.com/en-us/library/system.diagnostics.eventing.reader.standardeventlevel%28v=vs.110%29.aspx).


Read more about the [System.Diagnostics.Eventing.Reader](http://msdn.microsoft.com/en-us/library/system.diagnostics.eventing.reader%28v=vs.110%29.aspx) class.

And to know more about writing PowerShell conditions, you could read this [tutorial](http://www.powershellpro.com/powershell-tutorial-introduction/powershell-tutorial-conditional-logic/)

To use the xml query from a custom view in Windows Event Viewer,
simply copy the xml and paste into the Event Query field of the
event data source. Because we use a polling cycle to query the event
log, any TimeCreated filter will be replaced by us to avoid
duplicate events.

For example, a custom view that searches for events in the last hour,
with severity of Warning or Critical, and Ids of 104, 110-115, 155 will
result in the following XPath query:
[![][EventDatasourceXML.PNG]][EventDatasourceXML.png]


    <QueryList> 
        <Query Id="0" Path="Application">
            <Select Path="Application">*[System[(Level=1 or Level=3) and (EventID=104 or (EventID >= 110 and EventID <= 115) or EventID=155) and TimeCreated[timediff(@SystemTime) <= 3600000]]]</Select>
        </Query>
    </QueryList>

Simply copy this and paste into the eventlog datasource Event Query
field and save. We will convert the TimeCreated query and the following
filter will be used:

    <QueryList>
      <Query Id="0" Path="Application">
        <Select Path="Application">*[System[(Level=1  or Level=3) and (EventID=104 or  (EventID &gt;= 110 and EventID &lt;= 115)  or EventID=155) and TimeCreated[timediff(@SystemTime) &lt;= {time}]]]</Select>
      </Query>
    </QueryList>

`{time}` will be replaced by the number of milliseconds since the last
query automatically.

Note: The script to search for events and return relevant data is
approximately 3700 characters. Due to the Windows 8192 character limit
on the shell, any XML or PowerShell queries will need to be less than
4400 characters.

Note: The query for servers with .NET 3.5 and later uses the
Get-WinEvent PowerShell cmdlet. If your server does not have one of
these later versions, we will revert to using the Get-EventLog cmdlet.
It is recommended, but not required, to install .NET version 3.5 SP1 or
higher. If you have a mix of these servers using the same Event Log Data
Source, you can mix and match the differing powershell queries. e.g.
`{ $$_.Id -eq 4001 -or $$_.EventId -eq 4001 }`

To change event severity follow the steps: 

1.  Navigate to Event Classes, and click on */Status* event class. 
2.  Click *Add new EventClass Mappings* button.
3.  In the *Transform* section, add "`evt.severity = NUM`" where NUM is
    one of (0: Clear, 1: Debug, 2: Info, 3: Warning, 4: Error, 5: Critical)
    at the bottom 
4.  Click the *Save* button

### Custom Commands

You can use the custom command datasource in the
Windows ZenPack to create custom data points, graphs and thresholds.

-   Use either DOS shell commands or Powershell script
    *   Use any valid Windows executable or Powershell cmdlet.
    *   Powershell commands separated by `;`. Always end script with `;`.
    *   For tales eval, surround by single quotes. e.g. `'${here/id}'`.
    *   For Powershell variables, use 2 `$`. e.g. `$$myvar = 10`.
    *   There is a character limit of 8192 imposed by Microsoft.
        Zenoss header is \~450 characters so you have about 7500 characters
        for your script.
-   Use standard parser to parse the output or create your own
    *   Nagios have the form <key>=<value>.
    *   JSON - script must put data into JSON format.
    *   Auto will save a returned value into a data point.
    *   Create custom parser in $ZENOSS_HOME/Products/ZenRRD/parsers/.
-   Viewing script output
    *   Create datapoint(s) to collect the data for graphing.
    *   Create custom parser to send event or transform data.

#### Example usage

##### Script with TALES expression 

1.  Select a windows target device 
2.  Navigate to Device (/Server/Microsoft) 
3.  On the right side panel, click '+' to add a *Windows Shell* datasource 
4.  Provide name (eg. custom) and type (Windows Shell) for the datasource 
5.  Click *View Edit and Details*
6.  Set strategy to custom command 
7.  Set parser to Nagios
8.  Uncheck *Use Powershell*
9.  Set script to echo `OK^|value1=${here/zWinPerfmonInterval}`
10. Add data point to datasource called value1 which can be graphed

##### Using a custom parser

Logon to the zenoss server and create a python file called test1.py in /opt/zenoss/Products/ZenRRD/parsers and restart zenoss

The content of test1.py

```python
from Products.ZenRRD.CommandParser import CommandParser class
test1(CommandParser):
    def processResults(self, cmd, result):
        result.events.append({ 'summary':'test1 parser event', 'severity': 5, 'test1.detail': cmd.deviceConfig.name, })
```


1.  Select a windows target device.
2.  Navigate to the Device (/Server/Microsoft) Monitoring Template.
3.  On the Data Sources panel, click '+' to add a 'Windows Shell' datasource.
4.  Provide name (eg. custom) and type (Windows Shell) for the datasource.
5.  From the gear button, choose *View Edit and Details*.
6.  Set the strategy to Custom Command and Parser to test1
7.  Add a Windows command or Powershell script.
8.  Run zenpython to collect the data `zenpython run -v10 -d <devicename>`
9.  Check events after 5 minutes for the test1 event

##### Powershell Scripting using Auto parser

1.  Select a windows target device
2.  Navigate to Device (/Server/Microsoft)
3.  On the right side panel, click '+' to add a 'Windows Shell' datasource
4.  Provide name (eg. custom) and type (Windows Shell) for the datasource
5.  View Edit and Details : strategy ->custom command, parser is Auto, and tick the Use Powershell box
6.  Enter script. Be sure to use a double dollar sign, `$$`, in order to distinguish any powershell specific variables from a TALES expression.
7.  Add a datapoint to collect the return value from the script which you can then graph

### Configuring Service Monitoring

There are multiple ways to configure Windows service monitoring
depending on if you want to configure for a single service on a single
server, a specific service across all Windows servers, all 'Auto' start
services, or somewhere in between.

[![][winservice.png]][winservice.png]

Options 
:   Name: Enter a name for the data source
:   Enabled: Enable or disable the data source 
:   Severity: Choose the severity of the alert 
:   Cycle Time: Frequency of how often the datasource will query service status 
:   Update services immediately: Changes will be picked up during modeling. To have changes take effect immediately, check this box to start a job to index all services on all devices. This job could take several minutes to complete as it will update every service component on every Windows device in the system.
:   Service Options: Select the start type(s) to monitor. Add any services to include/exclude using a regex 
:   Service Status: Choose to be alerted if a service is either not Running, not Stopped, not Paused, not Running or Paused, or not Stopped or Paused.

See the following examples:

##### Manually Enable or disable monitoring for a single service on a single server.

1.  Navigate to the service on the server. 
2.  Click to select it.
3.  Select *Details* in the lower component pane. 
4.  Choose the Fail
5.  Severity. 
6.  Choose *Monitoring* from the gear menu. 
7.  Choose Yes or
8.  No depending on what you want.

Note: Once monitoring has been enabled or disabled for a service, no
monitoring template will apply. To reset this option for a service,
uncheck the 'Manually Selected Monitor State' box in the Details of the
service and save the change. This check box does not enable or disable
monitoring for the service component.

##### Enable monitoring by default for the WinRM service wherever it is enabled.

Option 1 
1.  Navigate to Advanced -\> Monitoring Templates. 
2.  Verify the list of templates is grouped by template. 
3.  Expand the *WinService* tree. 
4.  Click once to select the */Server/Microsoft* copy. 
5.  Choose *Copy / Override Template* from the Template gear menu at the bottom left of the page. 
6.  Select */Server/Microsoft (Create Copy)* from the target list then click submit. 
7.  Expand the resulting *copy_of_WinService* tree. 
8.  Select the */Server/Microsoft* copy.
9.  Choose *View and Edit Details* from the Template gear menu at the bottom left of the page. 
10. Change the template's name to *WinRM*.
11. Edit the datasource and optionally select the *Update services immediately* option. 
12. Tick the *Auto* checkbox under *Service Options* and click save.

Option 2
1.  Navigate to Infrastructure -> Windows Services.
2.  Locate the WinRM service.
3.  Select the start modes desired for this service.
4.  Enable monitoring by setting a Local Value.
5.  Optionally select a Local Failure Severity.
6.  Save.

Note: Setting a service to be monitored in this fashion will enable
monitoring for the service regardless of device class.

##### Enable/Disable monitoring by default for the WinRM service for a select group of servers. 

1.  Create a new device class somewhere under */Server/Microsoft/Windows* for the select group of servers. 
2.  Move the servers to the new device class. 
3.  Follow steps 1-5 from the previous section to create a copy of the WinService template. 
4.  Choose your new device class as the target then click submit. 
5.  Expand the *WinService* tree then select the copy in your device class. 
6.  Choose *View and Edit Details* from the gear menu at the bottom left of the page. 
7.  Change the template's name to *WinRM* then click submit.
8.  Double-click to edit the *DefaultService' datasource.
9.  Optionally select the *Update services immediately* option. This will start a background job that could take several minutes to complete for a large number of Windows devices. 
1.  Tick/Untick the *Auto* checkbox under *Service Options* and click save.

##### Enable monitoring of all services with a start mode of 'Auto'. 
1.  Navigate to Advanced -> Monitoring Templates. 
2.  Verify the list of templates is grouped by template. 
3.  Expand the *WinService* tree.
4.  Select */Server/Microsoft*. 
5.  In the Data Sources pane, click the + button to add a new data source, give it a name, and choose Windows Service as the type. 
6.  Choose *View and Edit Details* from the Data Sources gear menu. 
7.  Optionally select the *Update services immediately* option. This will start a background job that could take several minutes to complete for a large number of Windows devices. 
8.  Tick the *Auto* checkbox under *Service Options* and click save.

##### Create an organizer to monitor auto start SQL Server services. 
1.  Navigate to Advanced -> Monitoring Templates. 
2.  Verify the list of templates is grouped by template. 
3.  Expand the *WinService* tree. 
4.  Select */Server/Microsoft*. 
5.  In the Data Sources pane, click the + button to add a new data source, give it a name such as MSSQLSERVER, and choose Windows Service as the type. 
6.  Choose *View and Edit Details* from the Data Sources gear menu. 
7.  Optionally select the *Update services immediately* option. This will start a background job that could take several minutes to complete for a large number of Windows devices. 
8.  Tick the *Auto* checkbox under *Service Options*. 
9.  Enter *+MSSQLSERVER.** into the "Inclusions(+)/Exclusions(-)" text box and click save.

The order of precedence for monitoring a service is: 
1.  User manually sets monitoring.
2.  'DefaultService' datasource from the WinService template associated with the service.
3.  Datasource other than the DefaultService in the WinService template associated with the service.
4.  Monitoring is enabled via the Infrastructure -> Windows Services page.

Windows Service Startmodes (Template vs Windows Services)

| Startmodes | Template includes Service startmode | Template excludes Service startmode |
| ---------- | ----------------------------------- | ----------------------------------- |
| Windows Service Class includes Service startmode | monitored | monitored |
| Windows Service Class excludes Service startmode | monitored | NOT monitored|

Note: The Windows Service Template (default WinService) must have at
least one datasource enabled for monitoring to function.

You can optionally include or exclude certain services to be monitored
when selecting the *Auto*, *Manual*, and/or *Disabled* start
mode(s) by entering a comma separated list of services. These can be the
service names or a valid regular expression. Entered names and
expressions are case insensitive. To exclude services, you must specify
a '-' at the beginning of the name or regular expression. To include
services, specify a '+' at the beginning of the name or regular
expression. Exclusions will take precedence over inclusions, but the
exclusions must be placed before the wildcard *+.** inclusion.

Note: To enable monitoring by default of a service or services, you
must choose a start mode by ticking the appropriate box. Unticking all
three boxes disables monitoring by default.

Note: When saving changes to a service template and you choose to
update services immediately, this will create a job to index all
services on all devices. These changes may take several minutes to
propagate to all of your devices depending upon the size of your
organization. Updating is not recommended if you are making several
changes in a short period of time. Updates are automatically applied at
the time of the next model.

Note: The Windows Service datasource no longer depends on the
'DefaultService' data source name. User defined datasources are now
honored.

### DCDiag

Beginning with version 2.4.0, you can now monitor the output of DCDiag.
By default all dcdiag tests are enabled in the Active Directory
monitoring template. If a test fails an error event is issued. You can
also add other tests, such as DNS, and supply specific test parameters.

See [DCDiag](https://technet.microsoft.com/en-us/library/cc731968.aspx) for more
information.

Note: DCDiag must be run as a user with Administrator permissions. If
you will be monitoring a Domain Controller with a non administrator
user, you should disable these tests.

=== PortCheck ===

Beginning with version 2.4.0, you can now monitor specific ports in the
Windows Zenpack. By default, the ZenPack will monitor ports 9389, 3268,
3269, 88, 464, 389, 636, 445, 135, and 3389, as part of the Active
Directory monitoring template.

You can add and remove any port you wish to be monitored by editing the
PortCheck datasource in the Active Directory monitoring template.

To monitor ports on a Windows server that is not a domain controller,
simply create a new datasource and choose Windows PortCheck as the type.
Then add the ports you wish to monitor with a short description of each.

See [Active Directory port usage](https://technet.microsoft.com/en-us/library/dd772723%28v=ws.10%29.aspx)
for more information.

### WinRM Ping

WinRM Ping is a simple datasource that will attempt to retrieve basic
data over winrm. If the device cannot return a simple query, then Zenoss
will view this device as being down. An event will appear in the
/Status/Winrm/Ping event class with any resulting error message. This is
a more comprehensive test than using a ping. A simple ping test could
easily result in a false positive in many scenarios. The following are
just a few:

-   A target's IP has been reassigned to a non-Windows device between
    models.
-   The winrm service has stopped and cannot be restarted.
-   The monitoring user account password has expired.

This datasource is not enabled by default.

## Collector Daemons

*   zenpython

## Requirements

This ZenPack has the following requirements.

[PythonCollector ZenPack](/product/zenpacks/pythoncollector)
:   This ZenPack depends on PythonCollector being installed, and having the associated *zenpython* collector process running.

[ZenPackLib ZenPack](/product/zenpacks/zenpacklib)
:   This ZenPack depends on ZenPackLib being installed.

System Kerberos RPM
:   The operating system's kerberos RPM must be installed. See the [Installing Kerberos Dependency](#installing-kerberos-dependency) section for details.

Note: During ZenPack installation, a job to reindex Windows Services
may start. It is recommended to either stop zenjobs before installing or
to wait until the job finishes before restarting Zenoss. If you restart
before the job finishes, you may need to Abort and/or Delete the job
after the restart.

### Installing Kerberos Dependency

To use kerberos authentication the operating system's kerberos package
must be installed on all Zenoss servers. On Enterprise Linux (Red Hat
and CentOS) this is the *krb5-workstation* RPM and can typically be
installed by running the following command as the *root* user.

```text
yum -y install krb5-workstation
```

## Usage

##### Monitoring User Account

A monitoring user account must be either an Administrator or a least privileged user.

The Least Privileged User requires the following privileges and permissions:

-   Enable, Method Execute, Read Security, Remote Access to the following WMI namespaces 
    -   "Root"
    -   "Root/CIMv2" 
    -   "Root/DEFAULT"
    -   "Root/RSOP" 
    -   "Root/RSOP/Computer"
    -   "Root/WMI"
    -   "Root/CIMv2/Security/MicrosoftTpm" If IIS is installed, one of the following namespaces depending upon IIS version
        -   "Root/Webadministration" or "Root/microsoftiisv2"
-   Permission to use the winrm service
-   ReadPermissions, ReadKey, EnumerateSubKeys, QueryValues rights to the following registry keys 
    -   "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib"
    -   "HKLM:\system\currentcontrolset\control\securepipeservers\winreg"
    -   "HKLM:\SYSTEM\CurrentControlSet\Control\Class{4D36E972-E325-11CE-BFC1-08002bE10318}"
    -   "HKLM:\SYSTEM\CurrentControlSet\Services\Blfp\Parameters\Adapters"
    -   "HKLM:\Software\Wow6432Node\Microsoft\Microsoft SQL Server"
    -   "HKLM:\Software\Microsoft\Microsoft SQL Server"
-   Membership in the following local groups or domain level groups for a Domain Controller 
    -   "Performance Monitor Users"
    -   "Performance Log Users" 
    -   "Event Log Readers"
    -   "Distributed COM Users"
    -   "WinRMRemoteWMIUsers__"
-   “Read Folder” access to "C:\Windows\system32\inetsrv\config" if it exists
-   Each service needs the following permissions 
    -   SERVICE_QUERY_CONFIG
    -   SERVICE_QUERY_STATUS 
    -   SERVICE_INTERROGATE
    -   READ_CONTROL
    -   SERVICE_START

Note: An Administrator level user can be denied local logon and remote desktop access through a group policy object.

### Port Requirements

The ZenPack communicates with a Windows device over port 5985 for HTTP
or 5986 for HTTPS requests. Compatible ports of 80 and 443 are also
acceptable. For domain authentication, Kerberos communicates on port 88
of the KDC and on port 749 of the Admin Server.

Note: If using the compatibility ports of 80 or 443, you must create
the appropriate listener in your server's WinRM configuration.

### Adding a Windows Device

Use the following steps to start monitoring a Windows server using local
authentication in the Zenoss web interface.

1.  Navigate to the Infrastructure page.
2.  Select the Server/Microsoft/Windows device class.
    -   The Windows server must be added to this class or to a child of this class.
3.  Click Details and set the configuration properties for zWinRMUser and zWinRMPassword.
4.  Click See All.
5.  Choose *Add Single Device* from the add device button.
6.  Fill out the form.
    -   *Name or IP* must be resolvable and accessible from the collector server chosen in the *Collector* field.
7.  Click *ADD*.

------------------------------------------------------------------------

Alternatively you can use zenbatchload to add Windows servers from the
command line. To do this, you must create a text file with hostname,
username and password of all the servers you want to add. Multiple
endpoints can be added under the same
*/Devices/Server/Microsoft/Windows* section. Here is an example...

<syntaxhighlight lang="text"> /Devices/Server/Microsoft/Windows
win2008-1d.example.com zWinRMUser="Administrator",
zWinRMPassword="password" Win2012-1d.example.com
zWinRMUser="Administrator", zWinRMPassword="password" </syntaxhighlight>

You can then load the Windows servers into Zenoss Core or Resource
Manager as devices with the following command.

<syntaxhighlight lang="bash"> zenbatchload <filename> </syntaxhighlight>

### Configuration Options

The [Adding a Windows Device](adding-a-windows-device) steps shown above are for the simplest
case of using Windows local authentication. The following configuration
properties can be used to support monitoring other environments.

-   zWinRMUser
    :   The syntax used for zWinRMUser controls whether Zenoss
will attempt Windows local authentication or domain (kerberos)
authentication. If the value of zWinRMUser is *username*, local
Windows authentication will be used. If zWinRMUser is
*username@example.com*, domain authentication will be used. The
zWinKDC and potentially the zWinRMServerName properties become
important.

-   zWinRMPassword
    :   Password for user defined by *zWinRMUser*.

-   zWinKDC
    :   The zWinKDC property must be set if domain authentication is
        used. It must be the IP address or resolvable name of a valid Windows
        domain controller. To use multiple KDCs, you can enter a comma separated
        list of valid addresses or supply different KDCs across different Device
        Classes. See the Kerberos Tickets section for more information.

-   zWinTrustedRealm
    :   Enter the name of the domain which is trusted by the
        user's domain. This can be a child or other domain which has a trust
        relationship with the user's domain. For example, if zWinRMUser is
        *username@example.com*, and austin.example.com is a child of the
        example domain, enter *austin.example.com* into zWinTrustedRealm.

-   zWinTrustedKDC
    :   This property must be set if zWinTrustedRealm is set.
        It must be the IP address or resolvable name of a valid Windows domain
        controller for the trusted realm.

-   zWinRMServerName
    :   This property should only be used in conjunction
        with domain authentication when the DNS PTR record for a monitored
        server's managed IP address does not resolve to the name by which the
        server is known in Active Directory. For example, if myserver1 is known
        as myserver1.ad.example.com by Active Directory and is being managed by
        IP address 192.51.100.21, but 192.51.100.21 resolves to www.example.com,
        you will have to set zWinRMServerName to *myserver1.ad.example.com*
        for domain authentication to work.

    :   If many Windows servers in your environment don't have DNS PTR records
        that match Active Directory, it is recommended that you set the name of
        the Zenoss device's to be the fully-qualified Active Directory name and
        set zWinRMServerName to *${here/titleOrId}* at the
        /Server/Microsoft/Windows device class. This avoids the necessity of
        setting zWinRMServerName on every device.

    :   If the server name cannot be resolved and you are using domain
        authentication, it is recommended that you set the Id of the device to
        the IP address and the Title to the server name it is known by in Active
        Directory. Then use *${here/title}* for zWinRMServerName. This
        situation can occur when no DNS server is available. Kerberos always
        performs a reverse lookup when obtaining a ticket to use a service on a
        computer. If your servers are known by multiple names, the reverse
        lookup may return the wrong name and you will see "Server not found in
        kerberos database" errors. See the troubleshooting section on this topic
        for a solution.

-   zWinScheme
    :   This must be set to either *http* or *https*. The
        default is *http*.

-   zWinUseWsmanSPN
    :   If the HTTP/HTTPS service principals are exclusively
        in use for a particular service account, such as on an IIS server, set
        this option to true to use the WSMAN service principal name. You can use
        this option for all domain joined Windows Servers that are using a
        domain monitoring account.

    :   A domain controller may need “Validated write to service
        principal name” permission for the NETWORK SERVICE account in order for
        the WSMAN service principal name to be used.

-   zWinRMPort
    :   The port on which the Windows server is listening for
        *WinRM* or *WS-Management* connections. The default is *5985*. It
        is uncommon for this to be configured as anything else.

-   zWinPerfmonInterval
    :   The default interval in seconds at which
        *Windows Perfmon* datapoints will be collected. The default is *300*
        seconds or 5 minutes. It is also possible to override the collection
        interval for individual counters.

-   zWinKeyTabFilePath
    :   This property is currently used and reserved for
        future use when keytab files are supported.

-   zDBInstances
    :   This setting is only relevant when the
        *zenoss.winrm.WinMSSQL* modeler plugin is enabled. Multiple instances
        can be specified to monitor multiple SQL Server instances per server
        using different credentials. The default instance is *MSSQLSERVER*.
        Fill in the user and password to use SQL authentication. Leave the user
        and password blank to use Windows authentication. The default
        *MSSQLSERVER* credentials will be used for all instances not
        specified.

-   zWinRMEnvelopeSize
    :   This property is used when the winrm configuration
        setting for MaxEnvelopeSizekb exceeds the default of 512k. Some WMI
        queries return large amounts of data and this envelope size may need to
        be enlarged. A possible symptom of this is seeing an xml parsing error
        during collection.

-   zWinRMLocale
    :   The locale to use for communicating with a Windows
        server. The default is *en-US*. This property is reserved for future
        use.

-   zWinRSCodePage
    :   The code page which is in use on the Windows Server
        for the monitoring user account. The default is to use 65001, the
        identifier for unicode. The full list is here:
        https://msdn.microsoft.com/en-us/library/windows/desktop/dd317756(v=vs.85).aspx.
        To determine the code page in use on a Windows server, run
        `chcp` at a command prompt.

-   zWinRMKrb5includedir
    :   Optional directory which contains one or more
        kerberos configuration files. This is useful when extra kerberos options
        are needed, such as disabling reverse dns lookup. See
        http://web.mit.edu/kerberos/krb5-devel/doc/admin/conf\_files/krb5\_conf.html
        for a description of *includedir* and krb5.conf options available. The
        directory must exist and contain only kerberos configuration files. If
        the directory contains non-kerberos configuration files, it will be
        ignored.

-   zWinRMDisableRDNS
    :   Kerberos always performs a reverse lookup when obtaining a ticket to use the HTTP/HTTPS/WSMAN service principal.  If there are multiple names by which servers are known in your organization, or if you do not want to use reverse lookups, set this value to True.  Because this is a kerberos property, it can only be set one way or another.  You cannot mix and match this value and only the top level value at /Server/Microsoft will be honored.

-   zWinRMClusterNodeClass
    :   Path under which to create cluster nodes.  If you need to add cluster nodes to a specific class under the /Server/Microsoft/Windows device class, specify it with this property.  The default is /Server/Microsoft/Windows


Note: HyperV and MicrosoftWindows ZenPacks share krb5.conf file as
well as tools for sending/receiving data. Therefore if either HyperV or
Windows device has a correct zWinKDC setting, it will be used for
another device as well.

<br class="clear">

### Configuring MSSQL Server Modeling/Monitoring

##### Supported SQL Server versions
:   SQL Server 2005
:   SQL Server 2008
:   SQL Server 2008 R2
:   SQL Server 2012
:   SQL Server 2014
:   SQL Server 2016

Note: In order to properly monitor SQL Server, the Client Tools SDK must be installed for each version of SQL Server installed on your Windows servers.

##### Support for SQL Server and Windows Authentication: 
*   Windows Authentication: In *zDBInstances* property specify only SQL instances names, leave user and password fields blank. 
*   SQL Server Authentication: In *zDBInstances* property provide user name and password for each SQL instance. 
*   Specifying authentication per instance is no longer required with version 2.4.2 and above. We will use the credentials specified for the MSSQLSERVER instance by default.

Use the following steps to configure SQL Server Authentication on your SQL Server:
1.  Connect to SQL Instance using MSSQL Management Studio. 
2.  Select instance *Properties* > *Security* and make sure that *SQL Server and Windows Authentication mode* is enabled. 
3.  Open *Security* > *Logins*, select the user you specified in *zDBInstances* property or the *zWinRMUser* property if using Windows Authentication. 
4.  Check user *Properties* > *Status* and make sure that the user is Enabled. 
5.  Check user *Properties* > *Server Roles* and make sure that the user has the *public* role.
    a.  If using an Administrator user, make sure it has the *sysadmin* role. 
    b.  If not using an Administrator user, check user *Properties* > *Securables* and make sure the user has been granted *View server state* rights.

##### Support for Local and Failover Cluster SQL instances:

This ZenPack adds support for both local and failover cluster SQL Server
instances. Local SQL Server instances can be modeled/monitored within
windows devices (devices in *Server/Microsoft/Windows* device class).
SQL Server failover cluster instances can be modeled/monitored within
cluster devices (devices in *Server/Microsoft/Cluster* device class).

Use the following steps to model/monitor SQL Server instances: 
1.  Create a device in *Server/Microsoft/Windows* device class if you
    intend to model local SQL instances, or in *Server/Microsoft/Cluster*
    device class if you intend to model failover cluster instances. 
2.  Optionally specify the instance names to be modeled in *zDBInstances*
    zProperty. Provide user names and passwords if SQL Server Authentication
    is to be used. 
3.  Enable *zenoss.winrm.WinMSSQL* modeler plugin. 
4.  Remodel device.

##### SQL Server Monitoring

The monitoring templates for SQL Server are component templates so there
is no need to perform a bind. They will automatically be used to monitor
databases, instances, and jobs.

Note: The default instance of MSSQLSERVER appears as the host name.

Note: The authenticated user will need to be granted permission to
view the server state. For example, "GRANT VIEW SERVER STATE TO
'MYDOMAIN\zenoss_user'" or through the GUI in SQL Server Management
Studio. A Windows user must also be interactive, i.e. the account must not be
denied local logon rights.

### Working with WinCommand Notification Action

This ZenPack adds a new event notification action that can be used by
the zenactiond daemon to allow an arbitrary command to be executed on
the remote windows machine.

Use the following steps to set up a notification: 
1.  Select *Events* > *Triggers* from the Navigation Menu. 
2.  Create a trigger, selecting the rules that define it. 
3.  Select *Notifications* from the left panel. Add a new notification, enter a name for it and select *WinCommand* Action from the drop-down menu. Click Submit. 
4.  In the *Edit Notification* dialog on the *Notification* tab associate the 
    trigger with the notification and optionally select the notification
    properties (Enabled, Send Clear, Send only on Initial Occurrence, Delay,
    Repeat). 
5.  On the *Content* tab of the notification specify the 'Windows
    CMD Command* to run when configured triggers are matched. You may
    optionally specify *Clear Windows CMD Command* to run when the
    triggering event clears. 
6.  Submit changes.

For more information please refer to
[Working with Triggers and Notifications](http://community.zenoss.org/docs/DOC-10690)

## Setting up WinRM Service for Target Windows Machines

#### Group Policy

Navigate to Computer Configuration\Policies\Administrative Templates\Windows Components\Windows Remote Management

WinRMClient 
-   No setting changes required for client

WinRMService
-   Allow remote server management through WinRm

HTTP (Windows default is HTTPS see note below for more information)
-   Allow unencrypted Traffic (Only necessary when using basic authentication)

Basic Authentication (Windows default is Kerberos see note below for more information)
-   Allow Basic Authentication

WinRS Computer Configuration\Policies\Administrative Templates\Windows Components\Windows Remote Shell
-   Allow Remote Shell Access
-   Max number of processes per shell = 4294967295
-   Max number of shells per user = 2147483647
-   Shell Timeout = 7200000

#### Individual Machine configuration

-   Open ports 5985 (http)/5986(https) for WinRM
-   Run command prompt as Administrator
-   winrm quickconfig

-   winrm s winrm/config/service '@{MaxConcurrentOperationsPerUser="4294967295"}'
-   winrm s winrm/config/winrs '@{MaxShellsPerUser="2147483647"}'
-   winrm s winrm/config/winrs '@{IdleTimeout="7200000"}'

Basic Authentication (Windows default is Kerberos see note below for more information)
-   winrm s winrm/config/service/auth '@{Basic="true"}'
-   winrm s winrm/config/service '@{AllowUnencrypted="true"}'

Note: The above instructions use the max values for
MaxConcurrentOperationsPerUser and WinRS MaxShellsPerUser. If you do not
want to set these to the max, then a value of 50 should be adequate. The
default is 5 on both, which will cause problems because Zenoss will open
up concurrent requests for each WQL query and set of Perfmon counters.

Note: If you choose to use Basic authentication it is highly
recommended that you also configure HTTPS. If you do not use the HTTPS
protocol your user name and password will be sent over in clear text. If
you have challenges setting up HTTPS on the Windows clients but require
the user name and password to be encrypted, then using the Kerberos
authentication is the best option. HTTPS is not required for Kerberos
but is recommended. If you choose to use Kerberos authentication, then
your payload will be encrypted.

Note: If you are using kerberos on EL6 and higher to connect to your
Windows Server, your data will be encrypted over HTTP. For kerberos on
EL5, encryption is not supported so you must set the winrm
AllowUnencrypted option to true.

Note: If you choose to take the WinRM default configurations you must
supply Kerberos authentication settings in the zProperties. The Kerberos
authentication process requires a ticket granting server. In the
Microsoft Active Directory environment the AD Server is also the KDC.
The zWinKDC value must be set to the IP address of the AD Server and the
collector must be able to sent TCP/IP packets to this server. Once this
is set your zWinRMUserName must be a FQDN such as jsmith@Zenoss.com and
the zWinRMPassword must be set correctly for this user account.

Note: In order to use a single domain user in a child domain or other
trusted domain, set zWinKDC to the AD server of the user's domain. Then
enter the trusted domain name and associated AD server in the
zWinTrustedRealm and zWinTrustedKDC properties, respectively.

Note: The HTTPS setup must be completed on each client. At this time
we do not have notes on automating this task but are currently in the
process of testing several options. To successfully encrypt your payload
between the Zenoss server and the Windows client you must install a
Server Authentication certificate on the client machine. The process for
requesting and installing the appropriate certificate can be found at
the following URL.
http://blogs.technet.com/b/meamcs/archive/2012/02/25/how-to-force-winrm-to-listen-interfaces-over-https.aspx
Once the client has the correct certificate installed you only need to
change the zWinScheme to HTTPS and zWinRMPort to 5986. If you are still
having challenges setting up HTTPS on the client you can execute the
following command on any AD server to verify the appropriate SPN record
exists for Kerberos authentication.

<console> c:\>setspn -l hostname1 </console>

If you do not see a record with HTTPS/ at the beginning of the hostname
you can create the record, but this is not typically necessary as
Windows will use the HOST/ record as the default for most built in
services.  You can also use the zWinUseWsmanSPN property so that zenoss
will use the WSMAN service principal.  The WSMAN spn is created by
running *winrm quickconfig*.

<console> c:\>setspn -s HTTPS/hostname1.zenoss.com hostname1 </console>

Transitioning from WindowsMonitor
---------------------------------

If you are installing this ZenPack on an existing Zenoss system or
upgrading from an earlier Zenoss version you may have a ZenPack named
*ZenPacks.zenoss.WindowsMonitor* already installed on your system. You
can check this by navigating to Advanced -> ZenPacks.

This ZenPack functionally supersedes *ZenPacks.zenoss.WindowsMonitor*
for Windows platforms that support WinRM, but does not automatically
migrate monitoring of your Microsoft Windows resources when installed.
The ZenPacks can coexist gracefully to allow you time to manually
transition monitoring to the newer ZenPack with better capabilities.

1.  Navigate to the Infrastructure page.
2.  Expand the Server/Windows/WMI device class.
3.  Single-click to select a Windows device.
4.  Click the delete (*-*) button in the bottom-left.
5.  Click OK to confirm deleting the Windows device.
6.  Add the device back using the [Adding a Windows Device](#adding-a-windows-device) instructions above. Be sure to select the /Server/Microsoft/Windows device class and not the /Server/Windows/WMI device class.
7.  Repeat steps 3-6 for each Windows device.


Note: It is also possible to drag and drop selected Windows devices
from one class to another. You will need to remodel the devices after
the move.

## Limitations of Current Release

The current release is known to have the following limitations.

-   Support for team NICs is limited to Intel and Broadcom interfaces.
-   The custom widget for MSSQL Server credentials is not compatible
    with Zenoss 4.1.x, therefore the *zDBInstances* property in this
    version should be set as a valid JSON list (e.g. *[{"instance":
    "MSSQLSERVER", "user": "", "passwd": ""}]* ).
-   When upgrading to version 2.2.0, you may see a segmentation fault
    during the install. This occurs when upgrading from versions 2.1.3
    and previous. To ensure a successful installation, run the install
    once more and restart Zenoss.
-   Payload encryption is not supported on EL5 systems. This is due to
    the fact that the default kerberos library on EL5 systems does not
    contain the necessary functionality.
-   Current functionality for monitoring Server 2003 has not been
    removed from the ZenPack, but no future development will be done for
    Server 2003.
-   Starting with version 2.6.0 of the ZenPack, existing Windows Service
    components are no longer compatible. These will be removed upon
    installation. Once the device is modeled with the Services plugin
    enabled, Windows Service components will be discovered. Any existing
    monitoring templates will still apply. Any services that were
    manually selected to be monitored will not. See the section on
    [Configuring Service Monitoring](#configuring-service-monitoring).
-   The current release of this ZenPack uses the ZenPack SDK.  Some
    component classes have changed from pre-2.6.x versions of the ZenPack.
    During installation, the ZenPack will create a job that will update
    the Windows Devices and Components class types used by the SDK.
    Depending on your Zenoss instance resources, this job could take
    quite a while to complete.

A current list of known issues related to this ZenPack can be found with
[this JIRA query](https://jira.zenoss.com/issues/?jql=%22Affected%20Zenpack%28s%29%22%20%3D%20MicrosoftWindows%20AND%20status%20not%20in%20%28closed%2C%20%22awaiting%20verification%22%29%20ORDER%20BY%20priority%20DESC%2C%20id). You must be logged into JIRA to run this query. If you don't already have a JIRA account, you can [create one here](https://jira.zenoss.com/secure/Signup!default.jspa).

### Kerberos Tickets

The ZenPack will automatically generate a kerberos configuration file,
krb5.conf, in the \$ZENHOME/var/krb5/ directory. To use a custom
configuration file, place it in the \$ZENHOME/var/krb5/config/
directory. In Zenoss 5.x, this location is in a container so you will
need to be certain to commit any changes made. Upgrading Zenoss will
lose these changes, so you will need to update your container after
upgrade. The file name can be anything that contains alphanumeric,
dashes, and underscores.

To add a permanent location for you configuration file, you can make use
of the zWinRMKrb5includedir property. This must be a location accessible
from within a container and contain ONLY kerberos configuration file(s).
If the location is invalid or contains files other than kerberos
configuration files, it will be ignored and not added to the main
krb5.conf file.

Example:

A common problem with Kerberos is that a reverse DNS lookup will result
in multiple records returned, and not always the correct one. Kerberos
by default always performs a forward and reverse lookup when
establishing a ticket. To disable the reverse lookup, create a file in
either the default location or in a user specified location and add the
following:

<syntaxhighlight lang="text"> [libdefaults] rdns = false
</syntaxhighlight>

See [krb5.conf](http://web.mit.edu/kerberos/krb5-devel/doc/admin/conf_files/krb5_conf.html) 
for more information on the includedir and other kerberos options.

You can also supply multiple KDCs for a domain with the Windows ZenPack.
This can be done using either a comma separated list in the zWinKDC
property or supplying single KDCs for multiple devices or device classes
under the /Server/Microsoft device class.

This list also supports a simple regex to add, remove, and specify an
admin_server.

Adding a KDC
-   Use just the address or append a *+* to the beginning of the address to add a new kdc.

Removing a KDC
-   Append a *-* to the beginning of the KDC address to
    remove an existing KDC from the krb5.conf file. This can be used if a
    KDC is no longer in service or if the wrong address was entered
    previously. This can be removed from zWinKDC once a ticket granting
    ticket for the user has been obtained and the krb5.conf file is correct.

Specifying an admin_server
-   Optionally, use an asterisk, "*", to denote the admin_server. If none is provided, the first kdc in the list will be used. The admin_server is used for any admin work, such as changing a password through kinit.

For example, set zWinKDC to "*10.10.10.10,10.10.10.20,+10.10.10.30,-10.10.10.40" for specifying a
comma separated list. 10.10.10.10 will be a kdc and admin_server,
10.10.10.20 and 10.10.10.30 will be added as kdcs, and 10.10.10.40 is no
longer a valid kdc address and will be removed.

Note: Removing one or more errant KDCs from the system can be a time
consuming process, so we recommend double-checking that the addresses
are valid when entering them into the zWinKDC property.

## Service Impact

When combined with the Zenoss Service Dynamics product, this ZenPack
adds built-in service impact capability for services running on
Microsoft Windows. The following service impact relationships are
automatically added. These will be included in any services that contain
one or more of the explicitly mentioned entities.

#### Service Impact Relationships

The Windows server impacts the following:
-   File Systems 
-   Processes 
-   IP Services 
-   Processors 
-   Interfaces
-   Cluster Services 
-   Cluster Nodes 
-   Cluster Networks 
-   Windows Services 
-   HyperV 
-   SQL Server instances 
-   IIS Sites 
-   Hard Disks

-   Cluster Services impact Cluster Resources.
-   Cluster Interfaces and Disks impact Cluster Nodes.
-   Hard Disks impact File Systems.
-   SQL Server Instances impact SQL Databases, Backups, and Jobs.

## Troubleshooting

Please refer to the Zenoss Service Dynamics documentation if you run into any of the following problems:

-   ZenPack will not install
-   Adding a device fails
-   Don't understand how to add a device
-   Don't understand how to model a device

If you cannot find the answer in the documentation, then Resource
Manager (Service Dynamics) users should contact
[Zenoss Customer Support](https://support.zenoss.com). Core users can use
the #zenoss IRC channel or the community.zenoss.org forums (there is a
forum specific to Windows monitoring).

### Troubleshooting Windows

If you see 100% CPU usage on a domain controller and your forest
functional level is Windows 2003 or Windows 2008, you could be missing
the WinRMRemoteWMIUsers__ security group. Adding this group to your
domain should fix this problem. It is a known error from Microsoft,
[kb 3118385](https://support.microsoft.com/en-us/kb/3118385).

### Troubleshooting Kerberos Error Messages

<blockquote>
Cannot determine realm for numeric host address
</blockquote>

-   If you enter an IP address for the device id, make sure that the
    address is resolvable to a name. Common solutions to this is to use
    the zWinRMServerName property.

<blockquote>
Server not found in Kerberos database
</blockquote>

-   More often than not, this error indicates a DNS issue in which the
    domain controller is unable to locate the specified server by either
    IP address or name. The best solution varies over different domains
    and it is left to the user to decide which is best for their
    environment.

-   One solution is to disable reverse DNS lookups for kerberos. This can be
    achieved by setting the zWinRMDisableRDNS property to True.  If you use
    this option, you *MUST* only set it in at the /Server/Microsoft device class level.

-   You should also ensure that the correct name is returned for lookups.

<blockquote>
Preauthentication failed while getting initial credentials.
</blockquote>

-   This typically indicates a bad or expired password.

<blockquote>
Realm not local to KDC while getting initial credentials
</blockquote>

-   This indicates that one or more of the defined KDCs for a domain are
    incorrect. Add a *-* to the beginning of the errant KDC address to
    the beginning of the incorrect address in the zWinKDC property to
    remove it from the list of KDCs for a domain.

### Troubleshooting Kerberos Authentication with Wireshark

There are many reasons for kerberos authentication not to work, and a
lot of them result in the following unhelpful error message.

<blockquote>
kerberos authGSSClientStep failed (None)
</blockquote>

While Zenoss is unable to extract a useful error message when this
occurs, it turns out that Wireshark can get useful errors by looking at
the kerberos packets sent between Zenoss, your domain controller
(*zWinKDC*) and the monitored Windows server. Let's walk through an
example of using [Wireshark](http://www.wireshark.org/) to resolve an
*authGSSClientStep failed* error.

First install Wireshark on your system. It's GUI is easier to use than the command line equivalent.

Next you will need to create a packet capture file on your Zenoss server. Assuming the Windows server you're trying to monitor is *192.0.2.101* and the domain controller (*zWinKDC*) is *203.0.113.10*, you would run the following command as the root user on your Zenoss server.

<console>tcpdump -s0 -iany -w kerberdebug.pcap host 192.0.2.101 or host 203.0.113.10</console>

This will start capturing all packets to or from those two IP addresses. It will continue to capture these packets until you type *CTRL-C*.

Now you should attempt to remodel the Windows server where you're encountering the error. Once it completes, and fails, again you should go back to the terminal where tcpdump is running and type *CTRL-C*. You will now have a *kerberdebug.pcap* file in the directory where you ran the command.

Copy *kerberdebug.pcap* to your system where you installed Wireshark. Start Wireshark and open *kerberdebug.pcap*. You should see something like the following.

[![][windows-kerberos-wireshark.png]][windows-kerberos-wireshark.png]

You'll see that there's a *KRB5KRB_AP_ERR_SKEW* error. Searching
for this specific error code will quickly show that it occurs when the
kerberos client and server don't have their time's synchronized. There's
a tolerance for some difference, but in this case it was a big
difference due to misconfiguration.

There are some kerberos errors you'll see in the packets that a
completely normal part of negotiation and won't lead to any problems.
You should ignore the following errors shown in Wireshark:

-   *KRB5KRB_API_ERR_TKT_EXPIRED*: Zenoss will subsequently
    request a new ticket when this occurs.
-   *KRB5KRB_ERR_PREAUTH_REQUIRED*: This is a normal part of
    kerberos negotiation.
-   *KRB5KRB_ERR_RESPONSE_TOO_BIG*: Most requests won't fit in
    UDP. Zenoss will automatically switch to TCP.

You'll also see other kerberos messages that are normal. You should
ignore these kerberos messages shown by Wireshark:

-   *TGS-REQ*
-   *AS-REQ*

The following are the most common errors: 
-   *KRB5KRB_AP_ERR_SKEW*:
    -   As shown in the above example. A clock synchronization issue. 
-   *KRB5KDC_ERR_S_PRINCIPAL_UNKNOWN*
    -   This can happen if *zWinRMServerName* resolves to the server's IP address, but is not the name the server is known by in Active Directory. This will also be the error if you don't enter a *zWinRMServerName* and the reverse resolution of the device's manage IP address resolves to a name that doesn't match the server's name in Active Directory. Typical solutions to this are to add the name to the /etc/hosts file or to directly use the IP address of the server.

### Troubleshooting Services

If you see an event error that shows "The maximum number of concurrent
operations for this user has been exceeded", you will need to increase
the number of concurrent operations per user in the winrm config. For
example: 

```
winrm set winrm/config/service '@{MaxConcurrentOperationsPerUser="5000"}'
```

If you see an "Index out of range" error, this could indicate a low
number of available file handles in Linux. The default is 1024. To view
this information on your system, enter 'ulimit -n'. To increase this
limit, edit your /etc/sysctl.conf file and set fs.file-max to a
sufficiently large number. For example: 

```
vi /etc/sysctl.conf
fs.file-max=10000
```

### Troubleshooting monitoring

The first step in troubleshooting any monitoring issues is to scan the
zenpython log for errors.

While monitoring, possible network connectivity issues may occur while
trying to complete the Get-Counter command. If you experience
OperationTimeout errors, it may be a solution to decrease value of
*zWinPerfmonInterval* property to 30 seconds.

Other timeout issues on a domain could involve having a large Kerberos
token. This could be caused by the user belonging to a large number of
groups. See [kb 970875](https://support.microsoft.com/en-us/kb/970875) for more
information on the cause and resolution. Possible side effects of a
large token include high CPU usage on the Windows server.

If you see a corrupt counters error event, this indicates that the
specified counters have been corrupted on the Windows device. No data
will be collected for the specified counters until the counters have
been repaired on the device and zenpython has been restarted.

If you see the following error, check the zenhub log for errors:

```
Configuration for 10.111.5.171 unavailable -- is that the correct name?
```

### Troubleshooting modeling/monitoring

Version 2.6.0 introduces a command line option to save
modeling/monitoring results for troubleshooting. This option will save
the results returned from a Windows server from a modeler or datasource
plugin. This data can then be viewed/tested using unit tests to
determine issues.

Usage:

<syntaxhighlight lang="text"> 
export ZP_DUMP=1;zenmodeler run -d server1.example.com --collect=Interfaces; unset ZP_DUMP
</syntaxhighlight>

This will unload a pickle of the results to a file in the /tmp folder
called Interfaces_process_XXXXXX.pickle.

Note: Be sure to unset the environment variable to avoid unwanted
pickle files.

## Zenoss Analytics

This ZenPack provides additional support for Zenoss Analytics. Perform
the following steps to install extra reporting resources into Zenoss
Analytics after installing the ZenPack.

1.  Copy analytics-bundle.zip from <tt>\$ZENHOME/ZenPacks/ZenPacks.zenoss.Microsoft.Windows/ZenPacks/zenoss/Microsoft/Windows/analytics/</tt> on your Zenoss server.
2.  Navigate to Zenoss Analytics in your browser.
3.  From the Zenoss Instance list of options, select Internal Authentication.
4.  Login as an Analytics user with superuser privileges.
5.  Remove any existing *Microsoft Windows ZenPack* folder.
    a.  Choose *Repository* from the *View* menu at the top of the page.
    b.  Expand *Public* in the list of folders.
    c.  Right-click on *Microsoft Windows ZenPack* folder and choose *Delete*.
    d.  Confirm deletion by clicking *OK*.
6.  Add the new *Microsoft Windows ZenPack* folder.
    a.  Choose *Server Settings* from the *Manage* menu at the top of the page.
    b.  Choose *Import* in the left page.
    c.  Remove checks from all check boxes.
    d.  Click *Choose File* to import a data file.
    e.  Choose the analytics-bundle.zip file copied from your Zenoss server.
    f.  Click *Import*.

You can now navigate back to the *Microsoft Windows ZenPack* folder in
the repository to see the following resources added by the bundle.

##### Domains 
:   Microsoft Windows Domain 
:   Microsoft Cluster Domain

##### Ad Hoc Views
:   Windows IIS Peak Usage
:   Windows Interfaces Peak Usage

Domains can be used to create Ad Hoc views using the following steps.

1.  Choose *Ad Hoc View* from the *Create* menu.
2.  Click *Domains* at the top of the data chooser dialog.
3.  Expand *Public* then *Microsoft Windows ZenPack*.
4.  Choose the *Microsoft Windows Domain* domain

## Installed Items

Installing this ZenPack will add the following items to your Zenoss system.

Device Classes 
:   /Server/Microsoft 
:   /Server/Microsoft/Cluster 
:   /Server/Microsoft/Windows

Configuration Properties 
:   zWinRMUser 
:   zWinRMPassword 
:   zWinRMServerName 
:   zWinRMPort 
:   zDBInstances 
:   zWinKDC 
:   zWinKeyTabFilePath 
:   zWinScheme 
:   zWinPerfmonInterval 
:   zWinTrustedRealm 
:   zWinTrustedKDC 
:   zWinUseWsmanSPN 
:   zDBInstances 
:   zWinRMEnvelopeSize 
:   zWinRMLocale 
:   zWinRSCodePage 
:   zWinRMKrb5includedir

Modeler Plugins 
:   zenoss.winrm.CPUs 
:   zenoss.winrm.FileSystems 
:   zenoss.winrm.IIS 
:   zenoss.winrm.Interfaces 
:   zenoss.winrm.OperatingSystem 
:   zenoss.winrm.Processes 
:   zenoss.winrm.Routes 
:   zenoss.winrm.Services 
:   zenoss.winrm.Software 
:   zenoss.winrm.WinCluster 
:   zenoss.winrm.WinMSSQL

Datasource Types 
:   Windows EventLog 
:   Windows IIS Site 
:   Windows Perfmon 
:   Windows Process 
:   Windows Service 
:   Windows Shell 
:   Windows PortCheck

Monitoring Templates 
:   Device (in /Server/Microsoft) 
:   FileSystem (in /Server/Microsoft)
:   HardDisk (in /Server/Microsoft)
:   ethernetCsmacd (in /Server/Microsoft) 
:   OSProcess (in /Server/Microsoft) 
:   OSProcess-2003 (in /Server/Microsoft) 
:   WinService (in /Server/Microsoft) 
:   Active Directory (in /Server/Microsoft) 
:   Active Directory 2008 (in /Server/Microsoft) 
:   Active Directory 2008R2 (in /Server/Microsoft) 
:   IIS (in /Server/Microsoft) 
:   IISADMIN (in /Server/Microsoft) 
:   IISSites (in /Server/Microsoft) 
:   MSExchangeInformationStore (in /Server/Microsoft)
:   MSExchange2010IS (in /Server/Microsoft) 
:   MSExchange2013IS (in /Server/Microsoft) 
:   WinDBInstance (in /Server/Microsoft) 
:   WinSQLJob (in /Server/Microsoft) 
:   WinDatabase (in /Server/Microsoft) 
:   Cluster (in /Server/Microsoft) 
:   ClusterService (in /Server/Microsoft/Cluster)
:   ClusterResource (in /Server/Microsoft/Cluster) 
:   ClusterNode (in /Server/Microsoft/Cluster) 
:   ClusterNetwork (in /Server/Microsoft/Cluster) 
:   ClusterDisk (in /Server/Microsoft/Cluster)
:   ClusterInterface (in /Server/Microsoft/Cluster)

Changes
-------

2.7.0

-   Added support for Hard Disk association with storage servers
-   Added Session Management to lower number of connections to Windows Servers
-   Added option to specify winrm envelope size
-   Added ability to allow multiple KDCs for single domain
-   Added ability to specify user supplied kerberos configuration directory
-   Added support for Windows Server 2016
-   Added support for SQL Server 2014, 2016
-   Added Paused as valid Windows Service state to monitor
-   Added ability to disable rdns for kerberos
-   Improved support for SQL Server database Status
-   Fix ShellDataSource Doesn't Associate Event Severity or Class from Data Sources (ZPS-491)
-   Fix Modifying the WinService template causes parallel reindexing of the same components (ZPS-570)
-   Fix MicrosoftWindows - Device status become down after adding device using local authentication (ZPS-713)
-   Fix Windows ZP Does not allow compatible ports of 80/443 to be used (ZPS-622)
-   Fix Windows Zenpack may not properly detect IIS on 2012 servers. (ZPS-719)
-   Fix Long MSSQL Database names aren't parsed correctly because they exceed the powershell shell width (ZPS-944)

2.6.12

-   Fix ZenPack throws traceback when non windows data source is added (ZPS-661)

2.6.11

-   Fix Monitoring of SQL Instances results in a UUID error (ZPS-453)
-   Added additional event classes and handlers for Kerberos failures (ZEN-25700)

2.6.9

-   Added Auth event clears, getPingStatus includes /Status/Ping event class (ZEN-25700)
-   Fix Windows Shell Datasources are sending datamaps and bogging down ZenHub (ZEN-26226)

2.6.7

-   Fix TypeError during zenpython collection of a ShellDataSource (ZEN-25978)

2.6.6

-   Added additional event classes to cover connection errors (ZEN-25700)
-   Fix Windows Error Events come across as Info Events (ZEN-24633)
-   Fix Windows ZenPack - No "bad credentials" event for monitoring (ZEN-24726)
-   Fix MSSQL modeling doesn't pick up multiple instances if they're running different versions (ZEN-25851)
-   Fix Auto Creation of Windows Cluster Device doesn't copy over zWinKDC property (ZEN-25564)

2.6.5

-   Fix missing Process Set process title (ZEN-25311)

2.6.4

-   Fix Windows ZenPack incorrectly assumes that the first database returned is the master when modeling databases, backups, and jobs (ZEN-24519)
-   Fix WinRM ZenPack - WinService components disabled at template still show "Monitored" in component view (ZEN-24528)

2.6.3

-   Fix potential "clusternetworks" and "clusternodes" errors after upgrading (ZEN-24401)
-   Fix AttributeError: serviceclass on Windows Services after v515 update (ZEN-24347)
-   Fix duplicated "Interfaces" components after upgrade (ZEN-24401)

2.6.2

-   Fix WinRM ZenPack - Windows Services page elections conflict with WinService template exclusions (ZEN-24165)
-   Fix Modifying the WinService template causes parallel reindexing of the same components (ZEN-24375)

2.6.1

-   Fix Microsoft Windows ZenPack doesn't work with HyperV pack (ZEN-23967)
-   Fix Microsoft Windows:  no collection when Processes are modeled (ZEN-24010)
-   Fix Editing a Windows Service (WinService) Locks Up Zope and Times Out (ZEN-23827)

2.6.0

-   Enabled the use of the Infrastructure -> Windows Services page
-   Enabled domain authentication without the need for DNS
-   Added ability to dump results from plugins for troubleshooting
-   Converted to use zenpacklib
-   Document Microsoft Windows Event Log Monitoring Returns Information Events (ZEN-22904)
-   Fix zWinRMServerName not resolving properly on remote collector (ZEN-22880)
-   Fix WinRM ZP Error about concurrent shells doesn't close when not reoccuring (ZEN-23010)
-   Fix Latest version of WinRM pack (2.5.12) causes "AttributeError: in_exclusions" tracebacks (ZEN-23063)
-   Fix WinRM Interface modeler does not account for HP NIC naming scheme (ZEN-20762)
-   Fix WinRM monitoring does not emit message for expired password (ZEN-23183)
-   Fix Windows kinit: Internal credentials cache error while storing credentials while getting initial credentials (ZEN-23238)
-   Fix MSSQL Queries wrong database for metric (ZEN-23228)
-   Fix Windows Service shows 'Up' when down if event class modified (ZEN-19615)
-   Fix Windows Installed on UCS shows 2 interfaces where there's only 1 (ZEN-23379)
-   Fix Windows ZenPack, doesn't send Datasource fields in 'cmd' to Parsers (ZEN-23739)
-   Fix Windows Zenpack Impact relationships are inconsistent (ZEN-18648)
-   Fix WinRMPing datasource should be disabled by default (ZEN-23517)
-   Fix Copy Override of Windows template breaks EventLogDataSource query attribute (ZEN-23157)

2.5.13

-   Fix Active Directory not correctly detected (ZEN-23137)

2.5.12

-   Fix Windows EvenLog Datasource causes CPU 100% utilization (ZEN-20232)
-   Fix Windows Zenpack is improperly setting the Active Directory Template (ZEN-22369)

2.5.11

-   Fix MSSQL Monitoring (ZEN-22476)
-   Document Microsoft Windows:  High CPU usage when modeling domain controller (ZEN-22566)
-   Fix Windows Replication datasource fails for dcdiag user formatting (ZEN-22487)
-   Fix Microsoft Windows: failed collection - Couldn't bind: 24: Too many open files. (ZEN-22558)
-   Fix /Status/WinRM/Ping Event Class does not exist (ZEN-22407)

2.5.10

-   Fix Microsoft Windows Cluster datasources are sending datamaps too often and bogging down zenhub (ZEN-22345)

2.5.9

-   Fix Windows Team NIC Monitoring/Modeling Failure (ZEN-19588)

2.5.8

-   Fix ShellDataSource custom command does not send severity to custom parsers (ZEN-21928)

2.5.7

-   Fix Windows traceback during zenpack install (ZEN-21899)

2.5.6

-   Fix MicrosoftWindows - warning is generated if $$ is used in command datasource. (ZEN-20221)
-   Fix No event generated for failed modeling of Windows Device (ZEN-16195)
-   Fix Disabled WinRMService templates continue to event after disabling (ZEN-21603)

2.5.5

-   Fix WinRM Modeling Software Breaks if Installed Software Ends in Underscores(ZEN-20375)
-   Fix Microsoft Windows - monitoring cluster disks results in powershell error (ZEN-21325)
-   Fix Problem while executing plugin zenoss.winrm.FileSystems (ZEN-21351)
-   Fix Microsoft Windows - corrupt counters are not removed from collection (ZEN-21396)
-   Fix WinRM Polling causing partial Event Creation (ZEN-18757)

2.5.4

-   Fix Windows Service monitoring improvements
-   Fix WinRM Ping DataSource marks ping up devices down and stops all collection (ZEN-21270)
-   Fix WinCommand notification fails to run on WinRM ZP 2.5.1, 2.5.3 (ZEN-21272)

2.5.3

-   Fix Microsoft Windows - modeling cluster results in traceback error (ZEN-21242)

2.5.2

-   Fix IIS Site Failed connection when monitoring Windows Server 2012 with IIS 8.5 (ZEN-21029)

2.5.1

-   Fix MicrosoftWindows - Unbound Cluster Error when modeling cluster (ZEN-20931)
-   Fix MicrosoftWindows - list index out of range when modeling processes (ZEN-20932)
-   Fix MicrosoftWindows - Documentation typo mistakes (ZEN-20940)

2.5.0

-   Windows Service monitoring improvements
-   Added State column for MSSQL Databases
-   Improved EventLog querying to allow use of XPath XML
-   Enhancement Microsoft Windows - Update Cluster for failover cluster device (ZEN-18833)
-   Added ability to enter trusted domain information in order to use a single domain user
-   Documentation update:  Microsoft Windows - zenpython causes max cpu on target machine (ZEN-20542)
-   Fix Analytics not extracting software data on windows devices (ZEN-19366)
-   Fix Zenoss Windows Monitoring Spawning Thousands of Processes on Monitored Hosts (ZEN-18770)
-   Fix Microsoft Windows ZenPack -> Blank page is displayed when open 'Instance name' link in new page for My SQL Device (ZEN-15464)
-   Fix WinRM - ProcessDataSource.py results in "list index out of range" (ZEN-18823)
-   Fix Microsoft Windows ZenPack - MSSQL Databases: Unable to monitor any databases if any databases have ' in name (ZEN-18838)
-   Fix Microsoft Windows - Remove file systems with 0.00B Used/Free Bytes in File Systems component (ZEN-19213)
-   Fix Microsoft Windows - Cluster event is in Unknown class (ZEN-18835)
-   Fix Microsoft Windows - Database event is in Unknown class (ZEN-18836)
-   Fix Microsoft Windows - Provide a better message if using an event log that does not exist (ZEN-19270)
-   Fix Microsoft Windows - Remove IIS from default selected list of plugins (ZEN-19620)
-   Fix Microsoft Windows - an event " WinRS: get-clusterservice : The term 'get-clusterservice' is not recognized..." (ZEN-20138)
-   Fix Microsoft Windows - 'RecoveryModel' property is not displayed for SQL Enterprise 2005 (ZEN-20094)
-   Fix error when modeling hosts with IPv6 addresses. (ZEN-20474)
-   Fix WinRM for Windows server - Device Status should not use /Status/Ping (ZEN-19813)
-   Fix Wiki page for MicrosoftWindows ZenPack - IISAdmin service (ZEN-19300)
-   Fix WinRM Leaves Connections Open When Collection Fails Due to Native Language (ZEN-20514)
-   Fix WinRM - "The referenced context has expired" (ZEN-18115)
-   Fix Microsoft Windows - Windows cluster fails modeling for Task Scheduler traceback (ZEN-20438)

2.4.9

-   Fix Windows ZenPack - Cluster device does not add cluster nodes as devices on model (ZEN-19085)
-   Fix WinService - "list index out of range" error (ZEN-19452)

2.4.8

-   Fix Microsoft Windows Zenpack - MSSQLSERVER service shows as down but received event saying db instance was down (ZEN-19323)

2.4.7

-   Fix Microsoft Windows ZenPack - no data returned for databases in MSSQLSERVER default instance (ZEN-19282)
-   Fix Microsoft Windows ZenPack - services are not being monitored (ZEN-19284)

2.4.6

-   Fix Microsoft Windows ZenPack doesn't create events for MS SQL Jobs/Instances (ZEN-18680)
-   Fix WinRM Polling causing partial Event Creation (ZEN-18757)
-   Fix Microsoft Windows - Connection count is high (ZEN-18947)
-   Fix Microsoft Windows: DCDiag reports Access Denied during tests (ZEN-19188)

2.4.5

-   Fix MSSQL Components Generate Clear Event When PowerShell Script Fails (ZEN-18234)
-   Fix WinRM ZenPack missing thresholds which should be available out-of-box (ZEN-16024)
-   Fix Microsoft Windows - modeling MSSQLSERVER instance on 2012 cluster does not return databases, jobs, backups (ZEN-18811)
-   Fix Microsoft Windows ZenPack - WinMSSQL plugin breaks modeling (ZEN-18533)
-   Windows 2003 will no longer be supported

2.4.4

-   Fix extra points being sent into "Windows Shell" datasource parsers. (ZEN-18049)
-   With the ending of support by Microsoft for Windows 2003, this is the last version of the ZenPack to support Windows 2003.

2.4.3

-   Fix Port Checker in Microsoft Windows ZP 2.4.2 Results in Errors (ZEN-17893)


2.4.2

-   Fix poor performance of SQL Server monitoring of large number of databases. (ZEN-17535)
-   Fix poor performance of SQL Server modeling of large number of databases. (ZEN-17669)

2.4.1

-   Fixed Data from MS Exchange monitoring template is written to MSExchangeIS service component (ZEN-17566)

2.4.0

-   Added DCDiag tests for Active Directory monitoring
-   Added Port checking ability for Active Directory and other monitoring
-   Improved Kerberos error messages
-   Improved Custom Command feedback from Powershell scripts (ZEN-16834)
-   Improved automatic selection of device class monitoring templates to be run (ZEN-17059)
-   Fix Windows service datasource does not clear collection errors (ZEN-16802)
-   Fix EventLogDatasource ignores $max_age (ZEN-16564)
-   Fix Event Log Datasource does not escape tab characters (ZEN-15911)
-   Fix EventLogDataSource processes events from newest to oldest (ZEN-16565)
-   Fix WindowsEventLog will continuously fetch the same events generating false positives if the last event doesn't contain a message/summary (ZEN-17366)
-   Fix IIS-Request Rate graph should be removed from Graphs as it was divided into two (ZEN-17045)
-   Fix txwinrm:  Wrong number of arguments given (ZEN-16790)
-   Fix Some software is missing after model (ZEN-16574)
-   Fix OperatingSystem Modeler Broken (ZEN-16799)
-   Fix WinRM Software Modeler Parsing Traceback (ZEN-16224)
-   Fix Windows Zenpack Impact relationships are inconsistent (ZEN-16796)
-   Fix WinRM ZenPack missing thresholds which should be available out-of-box (ZEN-16024)
-   Fix No event generated for failed modeling of Windows Device (ZEN-16195)
-   Fix Microsoft Windows bad counter events in wrong event class (ZEN-16558)
-   Fix link is absent on Owner Node for Cluster/Services and Resources components (ZEN-15784)
-   Fix Microsoft Windows bad counter events in wrong event class (ZEN-16558)
-   Fix No event generated for failed modeling of Windows Device (ZEN-16195)
-   Fix WinRM ZenPack missing thresholds which should be available out-of-box (ZEN-16024)
-   Fix Microsoft.Windows - link is absent on Owner Node for Cluster/Services and Resources components (ZEN-15784)
-   Fix New Windows ZenPack - Working with templates throws 'NoneType' exception (ZEN-17318)
-   Fix Microsoft.Windows - unable to model device using Kerberos authentication on Centos 5 (ZEN-16546)
-   Fix Cannot "View and edit details"  on datasource Windows Eventlog (ZEN-17240)

2.3.2

-   Fix traceback during Software modeling (ZEN-16224)
-   Fix Event Log datasource ignoring max age field (ZEN-16564)
-   Fix Event log datasource does not escape tab characters (ZEN-15911)
-   Fix wrong number of arguments given (ZEN-16790)
-   Fix Powershell script not showing feedback on Custom Command datasource (ZEN-16834)
-   Fix traceback during Operating System modeling (ZEN-16799)

2.3.1

-   Fix significant memory leak when using kerberos authentication. (ZEN-16261)
-   Support "Wow6432Node" uninstall key for software inventory. (ZEN-16574)

2.3.0

-   Update Windows Service monitoring template to allow for monitoring by start mode
-   Fix memory leak with kerberos
-   Fix moving device to a different class

2.2.1

-   Fix Windows 2003 modeling/monitoring
-   Add log message during install
-   Re-authenticate through kerberos if connection is broken
-   Small bug fixes

2.2.0

-   Payload encryption over kerberos connections
-   Updated Events to use Get-WinEvent cmdlet
-   Updated Software modeler to query registry instead of Win32_Product
-   Updated FileSystems to show mapped network drives and mounted volumes
-   Support for Zenoss Analytics
-   Numerous bug fixes

2.1.3

-   Zenoss 5 compatibility fixes.

2.1.2

-   Added WinCommand notification action
-   Support for monitoring fail-over clustered MSSQL instances
-   Support for monitoring Windows event logs
-   Numerous bug fixes

2.1.0

-   Support for Service Impact
-   Support for Microsoft Exchange 2010 and Microsoft Exchange 2013
-   Ability to monitor Microsoft SQL Server using Windows Authenticated user
-   Fix Exchange 2007 counters
-   Fix cluster and node relationship
-   Fix virtual network adapter monitoring

2.0.3

-   Reduce possibility of gaps in perfmon collection. [ZEN-10600](https://jira.zenoss.com/browse/ZEN-10600)
-   Add zWinRMServerName property. [ZEN-9712](https://jira.zenoss.com/browse/ZEN-9712)
-   Support for IIS 7-8 without IIS 6 compatibility.
-   Honor sequence in process monitoring. [ZEN-10777](https://jira.zenoss.com/browse/ZEN-10777)
-   Fix cluster modeling for long server names. [ZEN-10572](https://jira.zenoss.com/browse/ZEN-10572)
-   Support TALES in Windows Shell custom command script. [ZEN-10426](https://jira.zenoss.com/browse/ZEN-10426)
-   Fix custom parser issue with Windows Shell datasource. [ZEN-10365](https://jira.zenoss.com/browse/ZEN-10365)
-   Handle null software install date. [ZEN-10361](https://jira.zenoss.com/browse/ZEN-10361)
-   Handle null process socket designation. [ZEN-10360](https://jira.zenoss.com/browse/ZEN-10360)
-   Model interface speed as integer. [ZEN-9608](https://jira.zenoss.com/browse/ZEN-9608)
-   Change WinRS success events from info to clear severity.
-   Fix leaking of active operations on Windows server.
-   Add missing counter details to missing counter events.
-   Fix Windows Shell collection on empty results.
-   Fix Windows Perfmon collection with cycletime > 600.

2.0.2

-   Fix build issue that made ZenPack unavailable from catalog.

2.0.1

-   Eliminate need for manual kerberos configuration on Enterprise Linux 5. [ZEN-9389](https://jira.zenoss.com/browse/ZEN-9389)
-   Fix "WinServiceLog: failed collection" error. [ZEN-9607](https://jira.zenoss.com/browse/ZEN-9607)
-   Provide more helpful error if AllowUnencrypted is disabled. [ZEN-9524](https://jira.zenoss.com/browse/ZEN-9524)

2.0.0

-   Initial release of new Windows support using WinRM instead of DCOM/RPC.

[Windows_device.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_device.png "Device" {.thumbnail}
[Windows_filesystem.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_filesystem.png "File System" {.thumbnail}
[Windows_graphs.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_graphs.png "Graphs" {.thumbnail}
[Windows_interfaces.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_interfaces.png "Interfaces" {.thumbnail}
[Windows_harddisk.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_.harddiskpng "Hard Disk" {.thumbnail}
[Windows_services.png]: /sites/default/files/zenpack/Microsoft Windows/Windows_services.png "Services" {.thumbnail}
[winservice.png]: /sites/default/files/zenpack/Microsoft Windows/winservice.png "WinService" {.thumbnail}
[CustomViewOptions.png]: /sites/default/files/zenpack/Microsoft Windows/CustomViewOptions.png "Custom View Options" {.thumbnail}
[CustomViewXML.png]: /sites/default/files/zenpack/Microsoft Windows/CustomViewXML.png "Custom View XML" {.thumbnail}
[EventDataSourceXML.png]: /sites/default/files/zenpack/Microsoft Windows/EventDataSourceXML.png "Event DataSource XML" {.thumbnail}
[windows-kerberos-wireshark.png]: /sites/default/files/zenpack/Microsoft Windows/windows-kerberos-wireshark.png "Wireshark" {.thumbnail}