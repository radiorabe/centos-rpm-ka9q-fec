# centos-rpm-libfec-odr
CentOS 7 RPM Specfile for [Opendigitalradio's fork of KA9Q's FEC library](https://github.com/Opendigitalradio/ka9q-fec) which is part of [RaBe's DAB / DAB+ broadcasting package collection](https://build.opensuse.org/project/show/home:radiorabe:dab).

## Usage

```bash
curl -o /etc/yum.repos.d/home:radiorabe:dab.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo
     
yum install libfec-odr
```
