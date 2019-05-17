from iconservice import *

TAG = 'PsudA'

class PsudA(IconScoreBase):

    def __init__(self, db: IconScoreDatabase):
        super().__init__(db)
        self._config = DictDB('config', db, value_type=str)

    def on_install(self):
        super().on_install()
        self._config['install_sender'] = str(self.msg.sender)
        self._config['install_owner'] = str(self.owner)
        self._config['send_tx_sender'] = str(self.msg.sender)
        self._config['send_tx_owner'] = str(self.owner)
        self._config['refer_tx_sender'] = str(self.msg.sender)
        self._config['refer_tx_owner'] = str(self.owner)
        self._config['is_real'] = 'Install'

    def on_update(self):
        super().on_update()
        self._config['install_sender'] = str(self.msg.sender)
        self._config['install_owner'] = str(self.owner)
        self._config['send_tx_sender'] = str(self.msg.sender)
        self._config['send_tx_owner'] = str(self.owner)
        self._config['refer_tx_sender'] = str(self.msg.sender)
        self._config['refer_tx_owner'] = str(self.owner)
        self._config['is_real'] = 'Update'

    @external(readonly=True)
    def getStore(self) -> str:
        _isinfo = dict()
        _isinfo['install_sender'] = str(self._config['install_sender'])
        _isinfo['install_owner'] = str(self._config['install_owner'])
        _isinfo['send_tx_sender'] = str(self._config['send_tx_sender'])
        _isinfo['send_tx_owner'] = str(self._config['send_tx_owner'])
        _isinfo['refer_tx_sender'] = str(self._config['refer_tx_sender'])
        _isinfo['refer_tx_owner'] = str(self._config['refer_tx_owner'])
        _isinfo['is_real'] = str(self._config['is_real'])
        return str(f'{_isinfo}')

    @external
    def setStore(self):
        self._config['send_tx_sender'] = str(self.msg.sender)
        self._config['send_tx_owner'] = str(self.owner)
        self._config['is_real'] = 'SetStore'

    @external
    def setStoreRefer(self, _value: str):
        self._config['refer_tx_sender'] = str(self.msg.sender)
        self._config['refer_tx_owner'] = str(self.owner)
        self._config['is_real'] = _value
