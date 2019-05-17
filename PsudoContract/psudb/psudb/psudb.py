from iconservice import *

TAG = 'PsudB'

class FunctionInterface(InterfaceScore):
    @interface
    def setStoreRefer(self, _value: str):
        pass

class PsudB(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()

    @external(readonly=True)
    def name(self) -> str:
        return "HelloWorld"

    @external(readonly=True)
    def hello(self) -> str:
        Logger.info('Hello, world!', TAG)
        return "Hello"

    @external
    def contractTest(self, _to: Address) -> None:
        recipient_score = self.create_interface_score(_to, FunctionInterface)
        recipient_score.setStoreRefer('value')
