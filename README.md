# sensugo-monitoring-setup-in-kubernetes
Want to know "How to run highly available sensugo cluster with external ETCD running within kubernetes cluster. Follow this tutorial.

## SensuGO Archtecture - Kubernetes
![SensuGoKubeArch](https://user-images.githubusercontent.com/38158144/62856678-39026f80-bd13-11e9-83fe-c91e5814378d.jpeg)

*Note* - Setup has been tried and tested on AWS EKS cluster - kubernetes version 1.11+ and in minikube 1.13+

## Prerequisites 
* Working kubernetes cluster with admin privilege.
* storageclass with the name `performace-retain` for volumes to be configured dynamically for `ETCD` and `InfluxDB`. Feel free to change it in the files or create one within cluster.

## Setup

#### Clone Repo
```
git clone https://github.com/tprakash17/sensugo-monitoring-setup-kubernetes.git
cd sensugo-monitoring-setup-kubernetes
```

Create Namespaces `sensugo` (we will run sensugo and etcd-cluster into this) and `influxdb` namespace is for deploying influxdb.
```
kubectl create ns sensugo
kubectl create ns influxdb
```

#### Deploy ETCD cluster
```
cd etcd
kubectl apply -f .
```

#### Deploy sensu-backend and as well as agent into `sensugo` namespace.
```
cd ../sensugo
kubectl apply -f .
```

## Extract metrics and visualisation using Grafana (Optional)

#### Deploy InfluxDB

```
cd ../influxdb-statefulset
```

Note - Before we deploy infgluxdb, we need to create dependent `configMap` and `secrets`. Please open the file `influxdb-statefulset.yaml` and read the header.

```
kubectl apply -f .
```

#### Deploy Grafana
```
cd ../grafana
kubectl apply -f .
```
