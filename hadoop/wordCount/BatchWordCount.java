package wordCount;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.operators.AggregateOperator;
import org.apache.flink.api.java.operators.DataSink;
import org.apache.flink.api.java.operators.DataSource;
import org.apache.flink.api.java.operators.FlatMapOperator;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;

public class BatchWordCount {
    //实现离线计算 DataSet
    public static void main(String[] args) throws Exception {
        //创建离线环境
        ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
        //创建Dataset
        DataSource<String> lines = env.readTextFile(args[0]);
        //切分压平
        FlatMapOperator<String, Tuple2<String, Integer>> wordAndOne = lines.flatMap(new FlatMapFunction<String, Tuple2<String, Integer>>() {
            @Override
            public void flatMap(String line, Collector<Tuple2<String, Integer>> out) throws Exception {
                String[] words = line.split(" ");
                for (String word : words) {
                    out.collect(Tuple2.of(word, 1));
                }
            }
        });
        //分组聚合 groupbb
        AggregateOperator<Tuple2<String, Integer>> result = wordAndOne.groupBy(0).sum(1);
        //将结果保存到HDFS
        DataSink<Tuple2<String, Integer>> tuple2DataSink = result.writeAsText(args[1]).setParallelism(1);
        //运行
        env.execute("BatchWordCount");
    }
}
