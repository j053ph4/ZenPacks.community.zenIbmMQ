
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
    
    ZC.MQQueuePanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'MQQueue',
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
                        "name": "getMqmanagerLink"
                    }, 
                    {
                        "name": "queueManager"
                    }, 
                    {
                        "name": "queueMaxDepth"
                    }, 
                    {
                        "name": "queueName"
                    }, 
                    {
                        "name": "queueType"
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
                        "header": "MQ Manager", 
                        "renderer": "pass_link", 
                        "id": "getMqmanagerLink", 
                        "dataIndex": "getMqmanagerLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Manager", 
                        "renderer": "pass_link", 
                        "id": "queueManager", 
                        "dataIndex": "queueManager"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Max Depth", 
                        "renderer": "pass_link", 
                        "id": "queueMaxDepth", 
                        "dataIndex": "queueMaxDepth"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Name", 
                        "renderer": "pass_link", 
                        "id": "queueName", 
                        "dataIndex": "queueName"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Type", 
                        "renderer": "pass_link", 
                        "id": "queueType", 
                        "dataIndex": "queueType"
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
            ZC.MQQueuePanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('MQQueuePanel', ZC.MQQueuePanel);
    ZC.registerName('MQQueue', _t('MQ Queue'), _t('MQ Queues'));
    
    })();

