import requests

# �X�}�[�g�t�H���ۗL���̓��v���擾����v���O����
# �g�p�f�[�^: �S��������Ԓ����ie-Stat�j
# �G���h�|�C���g: https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
# ���v�\ID(statsDataId)�F0003345395
# �ړI�F�X�}�[�g�t�H���ۗ̕L���ѐ��⊄�����擾
# �@�\�F
# - ���^���A���߁A����Ȃǂ��܂߂��f�[�^�擾
# - JSON�`���Ō��ʂ�\��

# API�L�[
APP_ID = "7092a46efe787eba5fa04e5a8dfa25e9a0cd9135"

# e-Stat API��URL
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# ���N�G�X�g�p�����[�^�ݒ�
params = {
    "appId": APP_ID,               # API�L�[
    "statsDataId": "0003345395",   # �X�}�[�g�t�H���ۗL�󋵂̓��v�\ID
    "lang": "J",                   # ���{��Ŏ擾
    "metaGetFlg": "Y",             # ���^�����擾
    "cntGetFlg": "N",              # ���������擾���Ȃ�
    "explanationGetFlg": "Y",      # ������擾
    "annotationGetFlg": "Y",       # ���߂��擾
    "sectionHeaderFlg": "1",       # �Z�N�V�����w�b�_�[��\��
    "replaceSpChars": "0"          # ���ꕶ���̕ϊ��Ȃ�
}

# API���N�G�X�g�𑗐M
response = requests.get(API_URL, params=params)

# ���X�|���X��JSON�`���ŕ\��
print(response.json())
