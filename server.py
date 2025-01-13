# Base
my_api_key = '1234'

headers = {
    "x-nxopen-api-key": my_api_key
  }

basic_link = "https://open.api.nexon.com"

# SERVER_LINK

# 계정 정보 조회
USER_FUNCTION = {'id': '/fconline/v1/id', # 계정 식별자(ouid)를 조회합니다.
                 'basic': '/fconline/v1/user/basic', # 기본 정보를 조회합니다.
                 'maxdivsion': '/fconline/v1/user/maxdivision', # 유저별 역대 최고 등급과 달성일자를 조회합니다.
                 'match': '/fconline/v1/user/match', # 유저의 매치 종류별 기록을 조회합니다.
                                                     # 유저가 플레이한 매치의 매치 고유 식별자 목록이 반환됩니다.
                                                     # 반환되는 매치 정보는 가장 최근 플레이한 매치부터 내림차순입니다.
                                                     # {offset} 과 {limit}을 사용하여 pagination이 가능합니다
                 'trade': '/fconline/v1/user/trade'} # 거래 종류{tradetype}로 유저의 이적시장 거래 종류별 기록을 조회합니다. (본인 거래 기록만 조회 가능)
                                                     # 유저가 거래한 선수의 아이디와 등급, 가치가 반환됩니다
                                                     # 반환되는 매치 정보는 가장 최근 거래이력부터 내림차순입니다
                                                     # {offset} 과 {limit}을 사용하여 pagination이 가능합니다

# 매치 정보 조회
MATHCH_FUNCTION = {'all': '/fconline/v1/match', # 모든 매치의 종류별 기록을 조회합니다.
                                                # 모든 매치의 매치 고유 식별자 목록이 반환됩니다.
                                                # 반환되는 매치 정보는 가장 최근 플레이한 매치부터 내림차순입니다.
                                                # {offset} 과 {limit}을 사용하여 pagination이 가능합니다.
                   'detail': '/fconline/v1/match-detail'} # 매치 고유 식별자{matchid}로 매치의 상세 정보를 조회합니다.
                                                          # 매치 시점, 매치 종류와 매치에 참여한 유저의 상세한 매치 통계가 반환됩니다.
                                                          # 매치 통계가 생성되기 전에 상대방이 매치를 종료할 경우, 상대방의 매치 정보가 보이지 않을 수도 있습니다.

# 랭커 정보 조회
RANKER_FUNCTION = {'stats': '/fconline/v1/ranker-stats'} # TOP 10,000 랭커 유저가 사용한 선수의 20경기 평균 스탯을 조회합니다.
                                                         # 선수의 고유 식별자와 포지션의 목록으로 랭커 유저가 사용한 선수의 평균 스탯 기록을 조회할 수 있습니다.
                                                         # 한번에 너무 많은 선수목록을 입력할 경우 413 Request Entity Too Large 에러가 반환될 수 있습니다. (1회 50명 적합)

# 메타데이터 정보 조회
METADATA_FUNCTION = {'matchtype': '/static/fconline/meta/matchtype.json', # 매치 종류(matchtype) 메타데이터를 조회합니다.
                     'id': '/static/fconline/meta/spid.json', # 해당 API는 Path 정보만 제공합니다. 
                                                              # 선수 고유 식별자는 시즌 아이디 (seasonid) 3자리 + 선수 아이디 (pid) 6자리로 구성되어 있습니다.
                                                              # 시즌 아이디는 /metadata/seasonid API로 조회할 수 있습니다.
                     'sid': '/static/fconline/meta/seasonid.json', # 시즌 아이디는 선수가 속한 클래스를 나타냅니다.
                     'position': '/static/fconline/meta/spposition.json', # 선수 포지션(spposition) 메타데이터를 조회합니다.
                     'division': '/static/fconline/meta/division.json', # 등급 식별자(division) 메타데이터를 조회합니다.
                     'volta_division': '/static/fconline/meta/division-volta.json'} # 볼타 공식경기의 등급 식별자(division) 메타데이터를 조회합니다.

# 이미지 정보 조회
IMAGE_FUNCTION = {'spid_action': '/live/externalAssets/common/playersAction/p{spid}.png', # 선수 고유 식별자(spid)로 선수의 액션샷 이미지를 가져옵니다. 
                  'pid_action': '/live/externalAssets/common/playersAction/p{pid}.png', # pid 로 선수의 액션샷 이미지를 가져옵니다. (ex. "000401" 일 경우 "401"로 조회)
                  'spid_image': '/live/externalAssets/common/players/p{spid}.png', # 선수 고유 식별자(spid)로 선수의 이미지를 가져옵니다.
                  'pid_image': '/live/externalAssets/common/players/p{pid}.png'} # pid로 선수의 이미지를 가져옵니다. (ex. "000401" 일 경우 "401"로 조회)