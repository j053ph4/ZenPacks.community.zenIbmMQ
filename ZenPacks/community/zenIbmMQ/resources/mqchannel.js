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
                        fields: [
            {name: 'uid'},
            {name: 'severity'},
            {name: 'status'},
            {name: 'name'},{name: 'channelManager'},
                {name: 'channelType'},
                {name: 'channelName'},
                {name: 'channelConn'},
                {name: 'channelStatus'},
                
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
                    id: 'channelManager',
                    dataIndex: 'channelManager',
                    header: _t('Manager'),
                    sortable: true,
                    width: 133
                },{
                    id: 'channelType',
                    dataIndex: 'channelType',
                    header: _t('Type'),
                    sortable: true,
                    width: 133
                },{
                    id: 'channelName',
                    dataIndex: 'channelName',
                    header: _t('Name'),
                    sortable: true,
                    width: 133
                },{
                    id: 'channelConn',
                    dataIndex: 'channelConn',
                    header: _t('Connection'),
                    sortable: true,
                    width: 133
                },{
                    id: 'channelStatus',
                    dataIndex: 'channelStatus',
                    header: _t('State'),
                    sortable: true,
                    width: 133
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
                    ZC.MQChannelPanel.superclass.constructor.call(this, config);
                }
            });
            
            Ext.reg('MQChannelPanel', ZC.MQChannelPanel);
            ZC.registerName('MQChannel', _t('MQ Channel'), _t('MQ Channels'));
            
            })(); 

