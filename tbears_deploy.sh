#!/bin/bash

echo .
echo 'Deploy PSUDO A...'
tbears deploy -k Keystore/test_001.json -p op0023@OP0023 PsudoContract/psuda/psuda/
echo .
echo .
echo 'Deploy PSUDO B...'
tbears deploy -k Keystore/test_001.json -p op0023@OP0023 PsudoContract/psudb/psudb/
echo .
