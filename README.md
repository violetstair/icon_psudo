# Score에서 다른 Score 호출하기 Test Code

> Score A에서 Score B를 호출할 떄

Score A
```python
class FunctionInterface(InterfaceScore):
    @interface
    def function_b(self, _from: Address, _value: int):
        pass

class ScoreA(IconScoreBase):
    def function(self, _from: Address, _to: Address, _value: int, _data: bytes):
        ...
        recipient_score = self.create_interface_score(_to, FunctionInterface)
        recipient_score.function_b(_from, _value)
```

Score B
```python
class ScoreB(IconScoreBase):
    def function_b(self, _from: Address, _value: int):
        pass
```

Result
```json
{
    "install_sender": "hxef97b900fa64dbb3c0e0ce76c4fb63b61d2aaf49",
    "install_owner": "hxef97b900fa64dbb3c0e0ce76c4fb63b61d2aaf49",
    "send_tx_sender": "hxef97b900fa64dbb3c0e0ce76c4fb63b61d2aaf49",
    "send_tx_owner": "hxef97b900fa64dbb3c0e0ce76c4fb63b61d2aaf49",
    "refer_tx_sender": "cx92e8a4908ddd4eb6d9fd36d6d77fa3613a102892",
    "refer_tx_owner": "hxef97b900fa64dbb3c0e0ce76c4fb63b61d2aaf49",
    "is_real": "value"
}
```
이때 호출되는 Score B에서의 self.msg.sender(호출자)는 Score B의 score 주소가 된다.
(사용자가 아님)
