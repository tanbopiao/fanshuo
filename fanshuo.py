"""返朔（FANSHUO）· 版本回溯，快照回滚

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：版本回溯，快照回滚。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Fanshuo:
    """返朔（FANSHUO）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "FANSHUO"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.snapshots = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "fanshuo",
            "cn": "返朔",
            "code": self.CODE,
            "duty": "版本回溯，快照回滚",
            "mingwen": "返朔归元，旧历可复",
            "anchor": self.ANCHOR,
        }

    def snapshot(self, state):
        """拍快照留朔，返回朔号。"""
        import json
        self._seq += 1
        sid = "SHUO-%04d" % self._seq
        self.snapshots[sid] = json.dumps(state, ensure_ascii=False, sort_keys=True)
        self.events.append({"event": "snapshot", "sid": sid})
        return sid

    def rollback(self, sid):
        """返朔归元：回滚到指定朔号。"""
        import json
        if sid not in self.snapshots:
            raise KeyError("无此朔号： %s" % sid)
        state = json.loads(self.snapshots[sid])
        self.events.append({"event": "rollback", "sid": sid})
        return state
