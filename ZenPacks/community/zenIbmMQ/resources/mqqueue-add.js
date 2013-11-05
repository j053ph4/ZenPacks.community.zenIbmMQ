
(function() {
        
            function getPageContext() {
                return Zenoss.env.device_uid || Zenoss.env.PARENT_CONTEXT;
            }
        
            Ext.ComponentMgr.onAvailable('component-add-menu', function(config) {
                var menuButton = Ext.getCmp('component-add-menu');
                menuButton.menuItems.push({
                    xtype: 'menuitem',
                    text: _t('Add MQ Queue') + '...',
                    hidden: Zenoss.Security.doesNotHavePermission('Manage Device'),
                    handler: function() {
                        var win = new Zenoss.dialog.CloseDialog({
                            width: 300,
                            title: _t('Add MQ Queue'),
                            items: [{
                                xtype: 'form',
                                buttonAlign: 'left',
                                monitorValid: true,
                                labelAlign: 'top',
                                footerStyle: 'padding-left: 0',
                                border: false,
                                items:                         [
                            {
                                fieldLabel: 'Manager', 
                                allowBlank: 'false', 
                                name: 'queueManager', 
                                width: 260, 
                                id: 'queueManagerField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Max Depth', 
                                allowBlank: 'false', 
                                name: 'queueMaxDepth', 
                                width: 260, 
                                id: 'queueMaxDepthField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Name', 
                                allowBlank: 'false', 
                                name: 'queueName', 
                                width: 260, 
                                id: 'queueNameField', 
                                xtype: 'textfield'
                            }, 
                            {
                                fieldLabel: 'Type', 
                                allowBlank: 'false', 
                                name: 'queueType', 
                                width: 260, 
                                id: 'queueTypeField', 
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
                                        Zenoss.remote.zenIbmMQRouter.addMQQueueRouter(opts,
                                        function(response) {
                                            if (response.success) {
                                                new Zenoss.dialog.SimpleMessageDialog({
                                                    title: _t('MQ Queue Added'),
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

