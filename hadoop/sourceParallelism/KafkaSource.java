package sourceParallelism;

import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;

import java.util.Properties;

/**
 * 从KafkaSource，可以并行的Source,并且可以实现ExactlyOnce
 */
public class KafkaSource {
    public static void main(String[] args) throws Exception {
        //创建环境
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        //Kafka的配置
        Properties propertipes = new Properties();
        //指定Kafka的Broker地址
        propertipes.setProperty("bootstrap.servers", "hadoop102:9090,hadoop103:9092");
        //指定组ID
        propertipes.setProperty("group.id",args[0]);
        //如果没有记录偏移量，第一次从最开始消费
        propertipes.setProperty("auto.offset.reset", "earliest");
        //Kafka的消费者不自动提交偏移量
        propertipes.setProperty("enable,auto.commit", "false");

        //KafkaSource
        FlinkKafkaConsumer<String> kafkaSource = new FlinkKafkaConsumer<>(
                "wc10",
                //序列化方法
                new SimpleStringSchema(),
                propertipes
        );
        //Source
        DataStreamSource<String> lines = env.addSource(kafkaSource);
        //Sink
        lines.print();
        env.execute("KafkaSource");
    }
}
