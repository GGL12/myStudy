package mapreduce.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
//Mapper<LongWritable, Text, Text, IntWritable> 输入数据key类型 输入数据value类型 输出数据key类型 输出数据value类型
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private Text kWord = new Text();
    private IntWritable vCount = new IntWritable();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        //取第一行数据
        String line = value.toString();
        //对数据切割，形成 k-v形式输出
        for (String word : line.split(" ")) {
            kWord.set(word);
            context.write(kWord, vCount);
        }

    }
}
