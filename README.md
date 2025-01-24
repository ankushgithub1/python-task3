**Check whether the helm is installed or not.**
- helm version
**if not installed follow the below steps otherwise skip these steps**
- curl https://get.helm.sh/helm-v3.12.0-linux-amd64.tar.gz -o helm-v3.12.0-linux-amd64.tar.gz
- tar -zxvf helm-v3.12.0-linux-amd64.tar.gz
- sudo mv linux-amd64/helm /usr/local/bin/helm
- brew install helm
- helm version
**Apply the Kubernetes Manifests**
- kubectl apply -f deployment.yaml
- kubectl apply -f service.yaml
- kubectl apply -f ingress.yaml
- kubectl apply -f hpa.yaml

**Set up Prometheus and Grafana for Monitoring & Install Prometheus and Grafana Using Helm:**
***First, add the Helm repositories:***
- helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
- helm repo add grafana https://grafana.github.io/helm-charts
- helm repo update
**Deploy Prometheus:**
- helm install prometheus prometheus-community/kube-prometheus-stack

**expose the service publically from minikube**
- kubectl port-forward --address 0.0.0.0 svc/ankush-python-app-service 3001:80 &
- kubectl port-forward --address 0.0.0.0 svc/prometheus-grafana 3000:80 &



