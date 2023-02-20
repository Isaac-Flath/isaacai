# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/isaacai',
                'doc_host': 'https://Isaac-Flath.github.io',
                'git_url': 'https://github.com/Isaac-Flath/isaacai',
                'lib_path': 'isaacai'},
  'syms': { 'isaacai.all': {},
            'isaacai.dataloaders': { 'isaacai.dataloaders.DataLoaders': ('dataloaders.html#dataloaders', 'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.DataLoaders.__init__': ( 'dataloaders.html#dataloaders.__init__',
                                                                                   'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.DataLoaders.from_dataset_dict': ( 'dataloaders.html#dataloaders.from_dataset_dict',
                                                                                            'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.DataLoaders.show_batch': ( 'dataloaders.html#dataloaders.show_batch',
                                                                                     'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.collate_dataset_dict': ( 'dataloaders.html#collate_dataset_dict',
                                                                                   'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.get_dataloaders': ('dataloaders.html#get_dataloaders', 'isaacai/dataloaders.py'),
                                     'isaacai.dataloaders.sample_dataset_dict': ( 'dataloaders.html#sample_dataset_dict',
                                                                                  'isaacai/dataloaders.py')},
            'isaacai.initialization': { 'isaacai.initialization._lsuv_stats': ( 'initialization.html#_lsuv_stats',
                                                                                'isaacai/initialization.py'),
                                        'isaacai.initialization.lsuv_init': ('initialization.html#lsuv_init', 'isaacai/initialization.py')},
            'isaacai.models': { 'isaacai.models.conv': ('models.html#conv', 'isaacai/models.py'),
                                'isaacai.models.fully_connected': ('models.html#fully_connected', 'isaacai/models.py'),
                                'isaacai.models.get_model_conv': ('models.html#get_model_conv', 'isaacai/models.py'),
                                'isaacai.models.get_model_fc': ('models.html#get_model_fc', 'isaacai/models.py')},
            'isaacai.recording': { 'isaacai.recording.MetricsCB': ('recording.html#metricscb', 'isaacai/recording.py'),
                                   'isaacai.recording.MetricsCB.__init__': ('recording.html#metricscb.__init__', 'isaacai/recording.py'),
                                   'isaacai.recording.MetricsCB.after_batch': ( 'recording.html#metricscb.after_batch',
                                                                                'isaacai/recording.py'),
                                   'isaacai.recording.MetricsCB.cleanup_epoch': ( 'recording.html#metricscb.cleanup_epoch',
                                                                                  'isaacai/recording.py'),
                                   'isaacai.recording.ProgressCB': ('recording.html#progresscb', 'isaacai/recording.py'),
                                   'isaacai.recording.ProgressCB.before_epoch': ( 'recording.html#progresscb.before_epoch',
                                                                                  'isaacai/recording.py'),
                                   'isaacai.recording.ProgressCB.before_fit': ( 'recording.html#progresscb.before_fit',
                                                                                'isaacai/recording.py'),
                                   'isaacai.recording.ProgressCB.cleanup_epoch': ( 'recording.html#progresscb.cleanup_epoch',
                                                                                   'isaacai/recording.py')},
            'isaacai.trainer': { 'isaacai.trainer.CancelBatchException': ('trainer.html#cancelbatchexception', 'isaacai/trainer.py'),
                                 'isaacai.trainer.CancelEpochException': ('trainer.html#cancelepochexception', 'isaacai/trainer.py'),
                                 'isaacai.trainer.CancelFitException': ('trainer.html#cancelfitexception', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer': ('trainer.html#trainer', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.__init__': ('trainer.html#trainer.__init__', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer._fit': ('trainer.html#trainer._fit', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer._one_epoch': ('trainer.html#trainer._one_epoch', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.add_callbacks': ('trainer.html#trainer.add_callbacks', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.fit': ('trainer.html#trainer.fit', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.one_batch': ('trainer.html#trainer.one_batch', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.one_epoch': ('trainer.html#trainer.one_epoch', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.run_callbacks': ('trainer.html#trainer.run_callbacks', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.subclassing_method': ( 'trainer.html#trainer.subclassing_method',
                                                                                 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.summarize_callbacks': ( 'trainer.html#trainer.summarize_callbacks',
                                                                                  'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.summarize_model': ('trainer.html#trainer.summarize_model', 'isaacai/trainer.py'),
                                 'isaacai.trainer.Trainer.training': ('trainer.html#trainer.training', 'isaacai/trainer.py'),
                                 'isaacai.trainer.summarize_callbacks': ('trainer.html#summarize_callbacks', 'isaacai/trainer.py')},
            'isaacai.training': { 'isaacai.training.BasicTrainCB': ('training.html#basictraincb', 'isaacai/training.py'),
                                  'isaacai.training.BasicTrainCB.backward': ('training.html#basictraincb.backward', 'isaacai/training.py'),
                                  'isaacai.training.BasicTrainCB.get_loss': ('training.html#basictraincb.get_loss', 'isaacai/training.py'),
                                  'isaacai.training.BasicTrainCB.predict': ('training.html#basictraincb.predict', 'isaacai/training.py'),
                                  'isaacai.training.BasicTrainCB.step': ('training.html#basictraincb.step', 'isaacai/training.py'),
                                  'isaacai.training.BasicTrainCB.zero_grad': ( 'training.html#basictraincb.zero_grad',
                                                                               'isaacai/training.py'),
                                  'isaacai.training.DeviceCB': ('training.html#devicecb', 'isaacai/training.py'),
                                  'isaacai.training.DeviceCB.__init__': ('training.html#devicecb.__init__', 'isaacai/training.py'),
                                  'isaacai.training.DeviceCB.before_batch': ('training.html#devicecb.before_batch', 'isaacai/training.py'),
                                  'isaacai.training.DeviceCB.before_fit': ('training.html#devicecb.before_fit', 'isaacai/training.py'),
                                  'isaacai.training.MomentumTrainCB': ('training.html#momentumtraincb', 'isaacai/training.py'),
                                  'isaacai.training.MomentumTrainCB.__init__': ( 'training.html#momentumtraincb.__init__',
                                                                                 'isaacai/training.py'),
                                  'isaacai.training.MomentumTrainCB.zero_grad': ( 'training.html#momentumtraincb.zero_grad',
                                                                                  'isaacai/training.py'),
                                  'isaacai.training.NBatchCB': ('training.html#nbatchcb', 'isaacai/training.py'),
                                  'isaacai.training.NBatchCB.__init__': ('training.html#nbatchcb.__init__', 'isaacai/training.py'),
                                  'isaacai.training.NBatchCB.before_batch': ('training.html#nbatchcb.before_batch', 'isaacai/training.py')},
            'isaacai.utils': { 'isaacai.utils.Hook': ('utils.html#hook', 'isaacai/utils.py'),
                               'isaacai.utils.Hook.__del__': ('utils.html#hook.__del__', 'isaacai/utils.py'),
                               'isaacai.utils.Hook.__init__': ('utils.html#hook.__init__', 'isaacai/utils.py'),
                               'isaacai.utils.Hook.remove': ('utils.html#hook.remove', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks': ('utils.html#hooks', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks.__del__': ('utils.html#hooks.__del__', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks.__enter__': ('utils.html#hooks.__enter__', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks.__exit__': ('utils.html#hooks.__exit__', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks.__init__': ('utils.html#hooks.__init__', 'isaacai/utils.py'),
                               'isaacai.utils.Hooks.remove': ('utils.html#hooks.remove', 'isaacai/utils.py'),
                               'isaacai.utils.PPDict': ('utils.html#ppdict', 'isaacai/utils.py'),
                               'isaacai.utils.PPDict.__str__': ('utils.html#ppdict.__str__', 'isaacai/utils.py'),
                               'isaacai.utils.add_callback': ('utils.html#add_callback', 'isaacai/utils.py'),
                               'isaacai.utils.add_callbacks': ('utils.html#add_callbacks', 'isaacai/utils.py'),
                               'isaacai.utils.clean_ipython_hist': ('utils.html#clean_ipython_hist', 'isaacai/utils.py'),
                               'isaacai.utils.clean_memory': ('utils.html#clean_memory', 'isaacai/utils.py'),
                               'isaacai.utils.clean_traceback': ('utils.html#clean_traceback', 'isaacai/utils.py'),
                               'isaacai.utils.get_grid': ('utils.html#get_grid', 'isaacai/utils.py'),
                               'isaacai.utils.inplace': ('utils.html#inplace', 'isaacai/utils.py'),
                               'isaacai.utils.mask2idxs': ('utils.html#mask2idxs', 'isaacai/utils.py'),
                               'isaacai.utils.remove_callback': ('utils.html#remove_callback', 'isaacai/utils.py'),
                               'isaacai.utils.remove_callbacks': ('utils.html#remove_callbacks', 'isaacai/utils.py'),
                               'isaacai.utils.retrieve_global_name': ('utils.html#retrieve_global_name', 'isaacai/utils.py'),
                               'isaacai.utils.run_callbacks': ('utils.html#run_callbacks', 'isaacai/utils.py'),
                               'isaacai.utils.set_seed': ('utils.html#set_seed', 'isaacai/utils.py'),
                               'isaacai.utils.show_image': ('utils.html#show_image', 'isaacai/utils.py'),
                               'isaacai.utils.subplots': ('utils.html#subplots', 'isaacai/utils.py'),
                               'isaacai.utils.to_cpu': ('utils.html#to_cpu', 'isaacai/utils.py'),
                               'isaacai.utils.to_device': ('utils.html#to_device', 'isaacai/utils.py'),
                               'isaacai.utils.with_cbs': ('utils.html#with_cbs', 'isaacai/utils.py'),
                               'isaacai.utils.with_cbs.__call__': ('utils.html#with_cbs.__call__', 'isaacai/utils.py'),
                               'isaacai.utils.with_cbs.__init__': ('utils.html#with_cbs.__init__', 'isaacai/utils.py')},
            'isaacai.visualizations': { 'isaacai.visualizations.ActivationStatsCB': ( 'visualization.html#activationstatscb',
                                                                                      'isaacai/visualizations.py'),
                                        'isaacai.visualizations.ActivationStatsCB.__init__': ( 'visualization.html#activationstatscb.__init__',
                                                                                               'isaacai/visualizations.py'),
                                        'isaacai.visualizations.ActivationStatsCB.color_dim': ( 'visualization.html#activationstatscb.color_dim',
                                                                                                'isaacai/visualizations.py'),
                                        'isaacai.visualizations.ActivationStatsCB.dead_chart': ( 'visualization.html#activationstatscb.dead_chart',
                                                                                                 'isaacai/visualizations.py'),
                                        'isaacai.visualizations.ActivationStatsCB.plot_stats': ( 'visualization.html#activationstatscb.plot_stats',
                                                                                                 'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback': ( 'visualization.html#hookscallback',
                                                                                  'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback.__init__': ( 'visualization.html#hookscallback.__init__',
                                                                                           'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback.__iter__': ( 'visualization.html#hookscallback.__iter__',
                                                                                           'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback.__len__': ( 'visualization.html#hookscallback.__len__',
                                                                                          'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback._hookfunc': ( 'visualization.html#hookscallback._hookfunc',
                                                                                            'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback.after_fit': ( 'visualization.html#hookscallback.after_fit',
                                                                                            'isaacai/visualizations.py'),
                                        'isaacai.visualizations.HooksCallback.before_fit': ( 'visualization.html#hookscallback.before_fit',
                                                                                             'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB': ('visualization.html#lrfindercb', 'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.__init__': ( 'visualization.html#lrfindercb.__init__',
                                                                                        'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.after_batch': ( 'visualization.html#lrfindercb.after_batch',
                                                                                           'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.after_fit': ( 'visualization.html#lrfindercb.after_fit',
                                                                                         'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.before_batch': ( 'visualization.html#lrfindercb.before_batch',
                                                                                            'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.before_fit': ( 'visualization.html#lrfindercb.before_fit',
                                                                                          'isaacai/visualizations.py'),
                                        'isaacai.visualizations.LRFinderCB.cleanup_fit': ( 'visualization.html#lrfindercb.cleanup_fit',
                                                                                           'isaacai/visualizations.py'),
                                        'isaacai.visualizations.append_stats': ( 'visualization.html#append_stats',
                                                                                 'isaacai/visualizations.py'),
                                        'isaacai.visualizations.get_hist': ('visualization.html#get_hist', 'isaacai/visualizations.py'),
                                        'isaacai.visualizations.get_min': ('visualization.html#get_min', 'isaacai/visualizations.py')}}}
