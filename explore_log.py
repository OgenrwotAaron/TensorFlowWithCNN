import pandas as pd
import matplotlib.pyplot as plt

log_data = pd.read_csv('training.log', sep=',', engine='python')

acc = log_data.accuracy
val_acc = log_data.val_accuracy
loss = log_data.loss
val_loss = log_data.val_loss

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label="Training accuracy")
plt.plot(epochs, val_acc, 'g', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.ylabel('Accuracy (1/10)')
plt.xlabel('epochs')
plt.legend(loc=0)
#plt.figure()

plt.show()
