(function(){
            var ZC = Ext.ns('Zenoss.component');
        
            function render_link(ob) {
                if (ob && ob.uid) {
                    return Zenoss.render.link(ob.uid);
                } else {
                    return ob;
                }
            }
        
            ZC.MQManagerPanel = Ext.extend(ZC.ComponentGridPanel, {
                constructor: function(config) {
                    config = Ext.applyIf(config||{}, {
                        componentType: 'MQManager',
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'managerStatus'},
                {name: 'managerName'},
                
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
                    id: 'managerStatus',
                    dataIndex: 'managerStatus',
                    header: _t('State'),
                    sortable: true,
                    width: 266
                },{
                    id: 'managerName',
                    dataIndex: 'managerName',
                    header: _t('Name'),
                    sortable: true,
                    width: 266
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
                    ZC.MQManagerPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('MQManagerPanel', ZC.MQManagerPanel);
            ZC.registerName('MQManager', _t('MQ Manager'), _t('MQ Managers'));
            
            })(); 

