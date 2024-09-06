##制作镜像及编译
echo "$1"
docker build  -f ./Dockerfile -t slotcraftinference ..

##添加镜像标签
echo "$2"
docker tag slotcraftinference harbor.rgstest.blugurugames.com/game/slotcraftinference/slotcraftinference:latest

##推送镜像
echo "$3"
docker push harbor.rgstest.blugurugames.com/game/slotcraftinference/slotcraftinference:latest