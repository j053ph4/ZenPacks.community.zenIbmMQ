
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.MQChannelPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'MQChannel',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "channelConn"
                    }, 
                    {
                        "name": "channelManager"
                    }, 
                    {
                        "name": "channelName"
                    }, 
                    {
                        "name": "channelStatus"
                    }, 
                    {
                        "name": "channelType"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "header": "Connection", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "channelConn", 
                        "dataIndex": "channelConn"
                    }, 
                    {
                        "header": "Manager", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "channelManager", 
                        "dataIndex": "channelManager"
                    }, 
                    {
                        "header": "Name", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "channelName", 
                        "dataIndex": "channelName"
                    }, 
                    {
                        "header": "State", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "channelStatus", 
                        "dataIndex": "channelStatus"
                    }, 
                    {
                        "header": "Type", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "channelType", 
                        "dataIndex": "channelType"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.MQChannelPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('MQChannelPanel', ZC.MQChannelPanel);
    ZC.registerName('MQChannel', _t('MQ Channel'), _t('MQ Channels'));
    
    })();

