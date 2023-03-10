* 从mmengine处fork
* 删除了计算机视觉等库的依赖
* 删除了不太可能使用到的功能
* 将COLLATE registry由函数变为类
* 删除DataPreprocessor相关，批量工作在COLLATE做
* 模型mode改为train（训练用）, eval（验证和测试用）, pred（默认方式，预测阶段用）
* DefaultOptimWrapperConstructor修改，重新整合params数据结构
* build_from_cfg新增关键字pretrained, 以此方式构建的对象设置init为True
* build_from_cfg中当type含有关键字AutoModel时，使用from_config构建
* init_cfg中pretrained > pretrained > init_module > init_cfg
* work_dir使用log_dir
* checkpoint改为目录，文件为目录中的ckpt.pth, save和resume只需要指定目录
* 更改resume和load逻辑
  * resume控制是否resume
  * load指定的文件加包含last_checkpoint则使用，否则需要指定具体，如：epoch_7