import requests

# ��t�s�̋C�ۃf�[�^���擾����v���O����
# �g�p�f�[�^: Tsukumijima.net API�i�V�C�\��j
# �G���h�|�C���g: https://weather.tsukumijima.net/api/forecast/city/120010
# �ړI�F��t�s�̋C�ۃf�[�^���擾
# �@�\�F
# - �����A�����A������̓V�C�A�C���A�~���m���Ȃǂ̃f�[�^���擾
# - JSON�`���Ō��ʂ�\��

# ��t�s�̓V�C�f�[�^���擾����API URL
API_URL = "https://weather.tsukumijima.net/api/forecast/city/120010"

# API���N�G�X�g�𑗐M
response = requests.get(API_URL)

# ���X�|���X��JSON�`���ŕ\��
print(response.json())
