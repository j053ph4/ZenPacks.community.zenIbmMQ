(function(){
            var ZC = Ext.ns('Zenoss.component');
        
            function render_link(ob) {
                if (ob && ob.uid) {
                    return Zenoss.render.link(ob.uid);
                } else {
                    return ob;
                }
            }
        
            ZC.MQQueuePanel = Ext.extend(ZC.ComponentGridPanel, {
                constructor: function(config) {
                    config = Ext.applyIf(config||{}, {
                        componentType: 'MQQueue',
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'queueType'},
                {name: 'queueName'},
                {name: 'queueManager'},
                {name: 'queueMaxDepth'},
                
            {name: 'usesMonitorAttribute'},
            {name: 'monitor'},
            {name: 'monitored'},
            {name: 'locking'},
            ]
        ,
                        columns:[{
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
        },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Name'),
            sortable: true,
            width: 70
        },{
                    id: 'queueType',
                    dataIndex: 'queueType',
                    header: _t('Type'),
                    sortable: true,
                    width: 160
                },{
                    id: 'queueName',
                    dataIndex: 'queueName',
                    header: _t('Name'),
                    sortable: true,
                    width: 160
                },{
                    id: 'queueManager',
                    dataIndex: 'queueManager',
                    header: _t('Manager'),
                    sortable: true,
                    width: 160
                },{
                    id: 'queueMaxDepth',
                    dataIndex: 'queueMaxDepth',
                    header: _t('Max Depth'),
                    sortable: true,
                    width: 160
                },{
            id: 'monitored',
            dataIndex: 'monitored',
            header: _t('Monitored'),
            sortable: true,
            width: 65
        },{
            id: 'locking',
            dataIndex: 'locking',
            header: _t('Locking'),
            renderer: Zenoss.render.locking_icons,
            sortable: true,
            width: 65
        }]
                    });
                    ZC.MQQueuePanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('MQQueuePanel', ZC.MQQueuePanel);
            ZC.registerName('MQQueue', _t('MQ Queue'), _t('MQ Queues'));
            
            })(); 

