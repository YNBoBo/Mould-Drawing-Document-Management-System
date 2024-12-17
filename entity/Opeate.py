class operate:
    def __init__(self, mould_id, operate_type, extra_msg, version_id, operate_date):
        self.mould_id = mould_id
        self.operate_type = operate_type
        self.extra_msg = extra_msg
        self.version_id = version_id
        self.operate_date = operate_date


processes = ['深孔钻', '数控铣', '高速铣', '侧铣', '线切割', '电火花', '精雕']

mould_parts = ['型腔', '型腔镶块', '型芯', '型芯镶块', '滑块', '镶块', '顶块']

operate_types = ['加工', '检查', '热流道', '终稿']
