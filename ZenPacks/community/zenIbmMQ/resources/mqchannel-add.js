
(function() {
        
            function getPageContext() {
                return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
            }
        
            Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
                var menuButton = Ext.getCmp('component-add-menu');
                menuButton.menuItems.push({
                    xtype: 'menuitem',
                    text: _t('Add MQ Channel') + '...',
                    hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
                    handler: function() {
                        var win = new Zenoss.dialog.CloseDialog({
                            width: 300,
                            title: _t('Add MQ Channel'),
                            items: [{
                                xtype: 'form',
                                buttonAlign: 'left',
                                monitorValid: true,
                                labelAlign: 'top',
                                footerStyle: 'padding-left: 0',
                                border: false,
                                items:                         [
                            {
                                fieldLabel: 'Connection', 
                                allowBlank: 'false', 
                                name: 'channelConn', 
                                width: 260, 
                                id: 'channelConnField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Manager', 
                                allowBlank: 'false', 
                                name: 'channelManager', 
                                width: 260, 
                                id: 'channelManagerField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Name', 
                                allowBlank: 'false', 
                                name: 'channelName', 
                                width: 260, 
                                id: 'channelNameField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'State', 
                                allowBlank: 'false', 
                                name: 'channelStatus', 
                                width: 260, 
                                id: 'channelStatusField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Type', 
                                allowBlank: 'false', 
                                name: 'channelType', 
                                width: 260, 
                                id: 'channelTypeField', 
                                xtype: 'textfield'
                            }
                        ]

                                ,
                                buttons: [{
                                    xtype: 'DialogButton',
                                    id: 'zenIbmMQ-submit',
                                    text: _t('Add'),
                                    formBind: true,
                                    handler: function(b) {
                                        var form = b.ownerCt.ownerCt.getForm();
                                        var opts = form.getFieldValues();
                                        Zenoss.remote.zenIbmMQRouter.addMQChannelRouter(opts,
                                        function(response) {
                                            if (response.success) {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    title: _t('MQ Channel Added'),
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK'),
                                                        handler: function() { 
                                                            window.top.location.reload();
                                                            }
                                                        }]
                                                }).show();
                                            }
                                        });
                                    }
                                }, Zenoss.dialog.CANCEL]
                            }]
                        });
                        win.show();
                    }
                });
            });
        }()
);

