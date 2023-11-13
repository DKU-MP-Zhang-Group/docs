## data management principals
1. your code should run under your own work space, usually that will be `/home/your_username`, you can use `cd ~` to go back to your work space.  
2. you can use `scp` to transfor your data from local computer to your workspace.  
3. for low frequently used data, such as saved checkpoints, previous datasets, please move them to `/mnt/sdb/your_username`(or `mnt/sdc/your_username` in some server). usually you have a folder named after your username. if you cannot find that, please contact [Tianyi](mailto:tianyi.zhang2@duke.edu)
4. unmodified datas(such as graduated student's resources, public datasets), can be moved to your Professor's nas. Prof.Zhang Lei's nas is `nas_77`, Prof. Yang's nas is `nas_75`. 