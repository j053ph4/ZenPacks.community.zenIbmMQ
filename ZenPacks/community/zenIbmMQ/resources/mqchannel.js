
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
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
                        "name": "getMqmanagerLink"
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
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Connection", 
                        "renderer": "pass_link", 
                        "id": "channelConn", 
                        "dataIndex": "channelConn"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Manager", 
                        "renderer": "pass_link", 
                        "id": "channelManager", 
                        "dataIndex": "channelManager"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Name", 
                        "renderer": "pass_link", 
                        "id": "channelName", 
                        "dataIndex": "channelName"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "State", 
                        "renderer": "pass_link", 
                        "id": "channelStatus", 
                        "dataIndex": "channelStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Type", 
                        "renderer": "pass_link", 
                        "id": "channelType", 
                        "dataIndex": "channelType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "MQ Manager", 
                        "renderer": "pass_link", 
                        "id": "getMqmanagerLink", 
                        "dataIndex": "getMqmanagerLink"
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

