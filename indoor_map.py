
from set_map import node, link, navi


# ocr 로 간판 문구 확인
start = "ff"

#시작 지점의 노드 확인
strt_node = node.name(start)

print('Start node = ', strt_node)

#목적지 입력 받기
fin = "bb"

fin_node = node.name(fin)
print('Final node = ', fin_node)

#경로 찾기
path = navi.path(strt_node,fin_node)

print("path =", path)


#경로 검출

#노드 간 거리 구하기

# strt_locat = link.locat(strt_node)
# fin_locat = link.locat(fin_node)
#
# print("strt_locat =",strt_locat)
# print("fin_locat =", fin_locat)

#경로에 따라 총 거리 구하기
dist,path_node = link.dist(path)
print("distance =", dist)
print("path_node =",path_node)

link = link.direction(path_node)

print("link =",link)