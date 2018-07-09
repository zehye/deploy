# settings.base
#   모든 설정 모듈 공통사항

# settings.local
#   runserver사용

# settings.dev
#   RDS, S3사용, debug메시지 출력

# settnigs.production
#   배포용 설정, Debug메시지 출력 안함
from .local import *
