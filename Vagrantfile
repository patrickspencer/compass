Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"

    config.vm.network :forwarded_port, guest: 80, host: 1234  # nginx
    config.vm.hostname = "example"

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", 512]
    end

    config.vm.provision :chef_solo do |chef|
        chef.cookbooks_path = "deploy/cookbooks"
        chef.roles_path = "deploy/roles"
        chef.json  = {
            :user => "vagrant",
            :servername => "example.example.com",
            :dbname => "example",
            :staticfiles => "/opt/example/apps/example/static/",
            :postgresql => {
                :password => {
                    :postgres  => "password"
                }
            },
            :users => [
                {
                    :name => "compass-webapp",
                    :key => "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEArIzjs/UHIogXxUG1jHGuZF98O9fPuGwovaHzGGVm061XeeszNguCXAVXMYK58zrYeaJSPG5/LbdiU9/cRXn+wYiniMTUxQoVnAJ9dMScO46rvsL+oR/90FAuv7rIaYrKTGKhCL2G2WEYduIqRc3CjcF0FsGoY7pYOTzLniKHNJ0z6N4OBrvhx/SDdqb86EuJqgJtMkl9vsjtBjsi27FPc8cOEMZEQWAvMK4NVQgeQvuNW86zl4vwEsjEUcI3Q7T790cofZGyKFbbhgxR5ew5c5hWgidDRruwEVdqhdfnzxHiAWJpd7G2QiHo2hrysh9K4mW56w2OFzs/i8GwBeV2fw== me@honza.ca"
                }
            ]
        }
        chef.add_role "webapp"
    end
end
