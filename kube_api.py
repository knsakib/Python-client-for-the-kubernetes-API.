from kubernetes import client, config
from flask import Flask, render_template

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

pod_ip_list=[] #created inital array/dict

pod_ip_list.append([]) #this is for pod ips
pod_ip_list.append([]) #this is for metadata.namespace
pod_ip_list.append([]) #this is for metadata.name



# pod_namespace_list = []
# pod_metadata_list = []

app = Flask(__name__)
v1 = client.CoreV1Api()
#print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)

@app.route("/")
def kube_api():
    for i in ret.items:
        #return i.metadata.name
        if i.status.pod_ip not in pod_ip_list[0]:
            pod_ip_list[0].append(i.status.pod_ip)
            pod_ip_list[1].append(i.metadata.namespace)
            pod_ip_list[2].append(i.metadata.name)
            # pod_ip_list[1].append(i.metadata.namespace)
            # pod_ip_list[2].append(i.metadata.name)

            #, i.metadata.namespace, i.metadata.name])
        # j=0
        # while(j<=3):
        #     pod_list[j]=[i.status.pod_ip, i.metadata.namespace, i.metadata.name]


    return render_template('template.html',
    pod_ip_list=pod_ip_list
    # pod_namespace_list=pod_namespace_list,
    # pod_metadata_list=pod_metadata_list
    )


if __name__ == "__main__":
    app.run()
