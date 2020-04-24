package com.hdfs;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.net.URI;

/**
 * 客户端API基本操作HDFS
 */
public class HDFSClient {
    //FileSystem是一个文件系统的实例，这个文件系统可以是hdfs，也可以是本地的文件系统
    private FileSystem fs;

    /**
     * 初始化文件系统
     * @throws IOException
     * @throws InterruptedException
     */
    @Before
    public void init() throws IOException, InterruptedException {
        fs = FileSystem.get(URI.create("hdfs://myhadoop101:9000"), new Configuration(),"user");
        System.out.println("初始化连接HDFS");
    }

    /**
     * 从本地上传文件到HDFS
     * @throws IOException
     */
    @Test
    public void put() throws IOException {
        fs.copyFromLocalFile(new Path("/data"), new Path("/HDFS/data"));
    }

    /**
     * 从HDFS下载文件到本地
     * @throws IOException
     */
    @Test
    public void get() throws IOException {
        fs.copyToLocalFile(new Path("/HDFS/data"), new Path("/data"));
    }

    /**
     * 查看文件的一些基本信息使用listStatus() and listFiles()方法(能查看到文件所在的块信息)
     * @throws IOException
     */
    @Test
    public void listStatus() throws IOException {
        FileStatus[] fileStatuses = fs.listStatus(new Path("/"));
        for (FileStatus fileStatus : fileStatuses) {
            if (fileStatus.isFile()) {
                System.out.println("这是一个文件的信息-------");
                System.out.println("路径:" + fileStatus.getPath());
                System.out.println("文件所有者" + fileStatus.getOwner());
            }else {
                System.out.println("这是一个文件夹的信息-------");
                System.out.println("路径" + fileStatus.getPath());
            }
        }
    }

    /**
     * 关闭资源连接
     * @throws IOException
     */
    @After
    public void after() throws IOException {
        System.out.println("关闭连接");
        fs.close();
    }
}
