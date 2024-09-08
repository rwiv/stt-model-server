cd ..
set IMG=ghcr.io/rwiv/stt-model-server:latest
set DOCKERFILE=./docker/Dockerfile-init

docker rmi %IMG%

docker build -t %IMG% -f %DOCKERFILE% .
docker push %IMG%

docker rmi %IMG%
pause