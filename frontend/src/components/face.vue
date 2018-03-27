<template>
    <div>
        <div style="width: 29%; height: 30%; border: 1px solid #000; position: absolute; right: 10px; top: 10px;">
            <!--<h2>{{ title2 }}</h2>-->
            <video width="100%" height="100%" autoplay :src="videostream" muted></video>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Face',
        data () {
            return {
                title1: 'Match',
                title2: 'User',
                title3: 'Logs',
                videostream: null,
                marginstream: null,
                logs: []
            }
        },

        sockets: {
            output_stream: function(data) {
                this.videostream = this.marginstream;
                this.marginstream = data;
            },
            output_log: function(data) {
                this.logs.unshift(data)
            }
        },

        created() {
        },

        mounted: function() {
            navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;

            if (navigator.getUserMedia) {
                window.URL = window.URL || window.webkitURL;

                navigator.getUserMedia({ video: true, audio: true }, (stream) => {
                    let mediaRecorder = new MediaRecorder(stream);

                    const rec = () => {
                        mediaRecorder.start();
                        setTimeout(() => {
                            mediaRecorder.stop();
                            rec();
                        }, 1000);
                    };

                    rec();

                    const socket = this.$socket;
                    mediaRecorder.ondataavailable = function(e) {
                        const blob = new Blob([e.data], { 'type' : 'video/webm' });
                        const fileReader = new FileReader();
                        fileReader.onload = function(event) {
                            const res = event.target.result;
                            socket.emit('input_stream', res);//res.substring(res.indexOf(';base64,') + 8));
                        };
                        fileReader.readAsDataURL(blob)
                    }

                }, (error) => {
                    console.log(error);
                });
            }
        }

    }
</script>
