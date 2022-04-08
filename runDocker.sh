docker stop tp4gbzg_cnt
docker container rm tp4gbzg_cnt
docker volume rm tp4gbzg_vol
docker image rm tp4gbzg_img
docker build -t tp4gbzg_img -f ./project/docker/Dockerfile .
docker volume create --name tp4gbzg_vol --opt device=$PWD --opt o=bind --opt type=none
docker run -d -p 5555:5555 --mount source=tp4gbzg_vol,target=/mnt/app/ --name tp4gbzg_cnt tp4gbzg_img