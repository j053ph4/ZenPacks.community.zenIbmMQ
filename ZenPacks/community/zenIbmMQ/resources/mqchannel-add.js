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
                                items: [
                {
                xtype: 'textfield',
                name: 'channelManager',
                fieldLabel: _t('Manager'),
                id: "channelManagerField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'channelType',
                fieldLabel: _t('Type'),
                id: "channelTypeField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'channelName',
                fieldLabel: _t('Name'),
                id: "channelNameField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'channelConn',
                fieldLabel: _t('Connection'),
                id: "channelConnField",
                width: 260,
                allowBlank: false,
                },
                
                {
                xtype: 'textfield',
                name: 'channelStatus',
                fieldLabel: _t('State'),
                id: "channelStatusField",
                width: 260,
                allowBlank: false,
                },
                ],
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
                                                        text: _t('OK')
                                                    }]
                                                }).show();
                                            }
                                            else {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    message: response.msg,
                                                    buttons: [{
                                                        xtype: 'DialogButton',
                                                        text: _t('OK')
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

