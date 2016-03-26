# slurm-utils
Utility scripts used with Slurm resource manager on Comet

# partstate

The `partstate` script is a simple wrapper for the Slurm `sinfo` command that produces output used for other tools.

Below is sample output for the @sdsc Comet cluster...

```
[admin@comet ~]$ partstate
Fri Mar 25 21:07:31 2016
       PARTITION  NODES    STATE  CPUS   S:C:T   MEMORY     JOB_SIZE     GRES      SHARE    TIMELIMIT
        compute*      6     down    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*    146     idle    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*   1379    alloc    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*    129      mix    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*     72     resv    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*     35     comp    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      2    down*    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      2   drain*    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      1     fail    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      7    drain    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      1     drng    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      4    maint    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
        compute*      8   maint*    24  2:12:1   128000         1-72   (null)  EXCLUSIVE   2-00:00:00
           debug      5     idle    24  2:12:1   128000          1-4   (null)         NO        30:00
           debug      3     resv    24  2:12:1   128000          1-4   (null)         NO        30:00
             gpu     14    alloc    24  2:12:1   128000          1-4    gpu:4  EXCLUSIVE   2-00:00:00
             gpu     11      mix    24  2:12:1   128000          1-4    gpu:4  EXCLUSIVE   2-00:00:00
             gpu      4     down    24  2:12:1   128000          1-4    gpu:4  EXCLUSIVE   2-00:00:00
             gpu      6    down*    24  2:12:1   128000          1-4    gpu:4  EXCLUSIVE   2-00:00:00
             gpu      1   maint*    24  2:12:1   128000          1-4    gpu:4  EXCLUSIVE   2-00:00:00
      gpu-shared      1     down    24  2:12:1   128000            1    gpu:4    FORCE:1   2-00:00:00
      gpu-shared      2    alloc    24  2:12:1   128000            1    gpu:4    FORCE:1   2-00:00:00
      gpu-shared     11      mix    24  2:12:1   128000            1    gpu:4    FORCE:1   2-00:00:00
      gpu-shared      5    down*    24  2:12:1   128000            1    gpu:4    FORCE:1   2-00:00:00
      gpu-shared      1   maint*    24  2:12:1   128000            1    gpu:4    FORCE:1   2-00:00:00
    large-shared      1     idle    64  4:16:1  1500000            1   (null)    FORCE:1   2-00:00:00
    large-shared      3    alloc    64  4:16:1  1500000            1   (null)    FORCE:1   2-00:00:00
          shared      1     down    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared     99     idle    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared    318    alloc    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared    137      mix    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared     10     resv    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared      1     comp    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared      2    down*    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared      5    drain    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared      1     drng    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
          shared      2   maint*    24  2:12:1   128000            1   (null)    FORCE:1   2-00:00:00
  ```

# whosonfirst

The `whosonfirst` script is a wrapper for the Slurm `sprio` command. As Comet uses the Slurm multifactor/priority plugin to help allocate resources to users it can be helpful to use this output to show the order that jobs waiting in the queue may be started. Since `sprio` doesn't currently provide options to sort the output this wrapper uses a fixed format so that the jobs can be sorted based on priority instead of by jobid.

Below is sample output from Comet...

NOTE: User names have been anonymized and large sequences of jobs from the same USER have been manually trimmed from the output. In these <snip> sequence the JOBID is normally sequential because users are submitting jobs in a loop. They typically have very similar PRIORITY often only differing by the AGE portion of the PRIORITY calculation.

```
[admin@comet ~]$ whosonfirst --partition=large
ORDER  JOBID    USER      PRIORITY  AGE   FAIRSHARE  JOBSIZE  PARTITION  QOS   NICE
1      1879306  seaforth  6080      79    4001       0        1000       1000  0
2      1879307  seaforth  6080      79    4001       0        1000       1000  0
...<snip>...
73     1888547  seaforth  6035      34    4001       0        1000       1000  0
74     1888550  seaforth  6035      34    4001       0        1000       1000  0
75     1887219  thirdeye  4723      40    2683       0        1000       1000  0
76     1887237  thirdeye  4722      39    2683       0        1000       1000  0
...<snip>...
80     1887673  thirdeye  4721      38    2683       0        1000       1000  0
81     1892664  thirdeye  4698      15    2683       0        1000       1000  0
82     1803792  twiceup   4047      1000  38         9        1000       2000  0
83     1803800  twiceup   4047      1000  38         9        1000       2000  0
...<snip>...
93     1827227  twiceup   3703      656   38         9        1000       2000  0
94     1827228  twiceup   3703      656   38         9        1000       2000  0
95     1730734  fivish    3000      1000  0          0        1000       1000  0
...<snip>...
98     1730742  fivish    3000      1000  0          0        1000       1000  0
99     1730750  fivish    3000      1000  0          0        1000       1000  0
100    1895642  fourteen  2519      0     520        0        1000       1000  0
101    1895643  fourteen  2519      0     520        0        1000       1000  0
102    1879407  bleu      2084      77    7          0        1000       1000  0
103    1879545  bleu      2083      77    7          0        1000       1000  0
104    1877554  tenthird  2081      81    0          0        1000       1000  0
105    1880215  less      2072      71    1          0        1000       1000  0
106    1880310  less      2071      70    1          0        1000       1000  0
107    1858728  umpir     1336      336   0          1        1000       0     0
108    1858730  umpir     1336      336   0          1        1000       0     0
...<snip>...
115    1858745  umpir     1336      336   0          1        1000       0     0
116    1858747  umpir     1336      336   0          1        1000       0     0
121    1870860  seventy   1216      196   20         1        1000       0     0
122    1870861  seventy   1216      196   20         1        1000       0     0
...<snip>...
124    1870863  seventy   1216      196   20         1        1000       0     0
125    1870864  seventy   1216      196   20         1        1000       0     0
126    1872209  schnelit  1176      176   0          1        1000       0     0
127    1872211  schnelit  1176      176   0          1        1000       0     0
128    1855879  santas    1157      147   10         1        1000       0     0
129    1875381  carrot    1130      130   0          1        1000       0     0
130    1814104  threeves  1114      114   0          1        1000       0     0
131    1880579  trekie    1105      69    36         0        1000       0     0
132    1880586  trekie    1105      69    36         0        1000       0     0
...<snip>...
158    1880736  trekie    1105      68    36         0        1000       0     0
159    1880743  trekie    1105      68    36         0        1000       0     0
160    1814086  threeves  1078      78    0          1        1000       0     0
161    1881057  cneale    1066      66    0          1        1000       0     0
162    1885914  santas    1055      45    10         1        1000       0     0
163    1893514  hushbby   1012      10    0          2        1000       0     0
164    1893517  hushbby   1012      10    0          2        1000       0     0
...<snip>...
557    1894507  hushbby   1007      5     0          2        1000       0     0
558    1894509  hushbby   1007      5     0          2        1000       0     0
559    1894511  tyreses   1007      5     0          2        1000       0     0
560    1894512  hushbby   1007      5     0          2        1000       0     0
561    1894515  tyreses   1007      5     0          2        1000       0     0
562    1894516  hushbby   1007      5     0          2        1000       0     0
563    1894518  hushbby   1007      5     0          2        1000       0     0
564    1894520  hushbby   1007      5     0          2        1000       0     0
565    1894521  tyreses   1007      5     0          2        1000       0     0
566    1894522  hushbby   1007      5     0          2        1000       0     0
567    1894525  tyreses   1007      5     0          2        1000       0     0
568    1894526  hushbby   1007      5     0          2        1000       0     0
569    1894527  tyreses   1007      5     0          2        1000       0     0
570    1894530  tyreses   1007      5     0          2        1000       0     0
571    1894532  hushbby   1007      5     0          2        1000       0     0
572    1894533  tyreses   1007      5     0          2        1000       0     0
573    1894535  hushbby   1007      5     0          2        1000       0     0
574    1894536  tyreses   1007      5     0          2        1000       0     0
575    1894538  tyreses   1007      5     0          2        1000       0     0
576    1894542  tyreses   1007      5     0          2        1000       0     0
577    1894543  hushbby   1007      5     0          2        1000       0     0
578    1894544  tyreses   1007      5     0          2        1000       0     0
579    1894546  hushbby   1007      5     0          2        1000       0     0
580    1894549  hushbby   1007      5     0          2        1000       0     0
...<snip>...
1013   1895551  hushbby   1002      0     0          2        1000       0     0
1014   1895553  hushbby   1002      0     0          2        1000       0     0
```
