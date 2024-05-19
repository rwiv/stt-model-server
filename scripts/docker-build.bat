cd ..

docker rmi stt-model-server
docker build -t stt-model-server:latest -f ./docker/Dockerfile .
pause
