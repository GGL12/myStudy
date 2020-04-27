package mapreduce.wordcount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    //初始化value
    private IntWritable vTotal = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int sum = 0;
        //对分组后的数据遍历求和
        for (IntWritable value : values) {
            sum += value.get();
        }
        //包装结果并输出T
        vTotal.set(sum);
        context.write(key, vTotal);
    }
}
